import asyncio
import importlib
import sys
import unittest

AsyncCache = importlib.import_module(sys.argv.pop(1)).AsyncCache


class ControlledLoader:
    def __init__(self):
        self.calls = []
        self.started = asyncio.Queue()

    async def __call__(self, key):
        future = asyncio.get_running_loop().create_future()
        self.calls.append((key, future))
        self.started.put_nowait(future)
        return await future

    async def next_call(self):
        return await asyncio.wait_for(self.started.get(), 2)


class CacheTests(unittest.IsolatedAsyncioTestCase):
    async def asyncSetUp(self):
        self.loader = ControlledLoader()
        self.cache = AsyncCache(self.loader)
        self.clients = []

    def get(self, key="k"):
        task = asyncio.create_task(self.cache.get(key))
        self.clients.append(task)
        return task

    async def settle(self):
        # Drain ready tasks on this one event loop; no wall-clock race guessing.
        for _ in range(6):
            await asyncio.sleep(0)

    async def asyncTearDown(self):
        for client in self.clients:
            client.cancel()
        await asyncio.gather(*self.clients, return_exceptions=True)
        for _, future in self.loader.calls:
            if not future.done():
                future.cancel()
        await self.settle()

    async def test_same_generation_coalesces_and_caches(self):
        clients = [self.get() for _ in range(12)]
        load = await self.loader.next_call()
        await self.settle()
        count = len(self.loader.calls)
        load.set_result(44)
        self.assertEqual(await asyncio.gather(*clients), [44] * 12)
        self.assertEqual(count, 1)
        self.assertEqual(await self.cache.get("k"), 44)
        self.assertEqual(len(self.loader.calls), 1)

    async def test_cancelled_caller_does_not_cancel_shared_load(self):
        first = self.get()
        load = await self.loader.next_call()
        second = self.get()
        await self.settle()
        first.cancel()
        with self.assertRaises(asyncio.CancelledError):
            await first
        self.assertFalse(load.cancelled())
        load.set_result(7)
        self.assertEqual(await second, 7)
        self.assertEqual(len(self.loader.calls), 1)

    async def interleaved_invalidation(self, fail_old=False):
        old_client = self.get()
        old_load = await self.loader.next_call()
        await self.cache.invalidate("k")
        new_client = self.get()
        new_load = await self.loader.next_call()
        if fail_old:
            old_load.set_exception(ValueError("old generation failed"))
            with self.assertRaises(ValueError):
                await old_client
        else:
            old_load.set_result(10)
            self.assertEqual(await old_client, 10)
        later_client = self.get()
        await self.settle()
        count = len(self.loader.calls)
        new_load.set_result(20)
        # A wrongly spawned third load returns a distinguishable value.
        for _, load in self.loader.calls[2:]:
            if not load.done():
                load.set_result(999)
        observed = await asyncio.gather(new_client, later_client)
        self.assertEqual((count, observed), (2, [20, 20]))
        self.assertEqual(await self.cache.get("k"), 20)

    async def test_old_success_preserves_new_flight(self):
        await self.interleaved_invalidation()

    async def test_old_failure_preserves_new_flight(self):
        await self.interleaved_invalidation(fail_old=True)

    async def test_stale_completion_cannot_overwrite_new_value(self):
        old_client = self.get()
        old_load = await self.loader.next_call()
        await self.cache.invalidate("k")
        new_client = self.get()
        new_load = await self.loader.next_call()
        new_load.set_result(20)
        self.assertEqual(await new_client, 20)
        old_load.set_result(10)
        self.assertEqual(await old_client, 10)
        self.assertEqual(await self.cache.get("k"), 20)
        self.assertEqual(len(self.loader.calls), 2)

    async def test_failure_can_be_retried(self):
        first = self.get()
        load = await self.loader.next_call()
        load.set_exception(ValueError("retry me"))
        with self.assertRaises(ValueError):
            await first
        second = self.get()
        retry = await self.loader.next_call()
        retry.set_result(9)
        self.assertEqual(await second, 9)
        self.assertEqual(len(self.loader.calls), 2)

    async def test_different_keys_load_concurrently(self):
        a = self.get("a")
        load_a = await self.loader.next_call()
        b = self.get("b")
        load_b = await self.loader.next_call()
        self.assertFalse(load_a.done())
        load_b.set_result(2)
        self.assertEqual(await b, 2)
        load_a.set_result(1)
        self.assertEqual(await a, 1)


if __name__ == "__main__":
    unittest.main(verbosity=2)
