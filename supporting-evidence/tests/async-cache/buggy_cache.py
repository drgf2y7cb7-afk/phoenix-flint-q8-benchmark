"""An asynchronous per-key cache with coalesced loads and invalidation."""
import asyncio


class AsyncCache:
    def __init__(self, loader):
        self._loader = loader
        self._values = {}
        self._flights = {}
        self._epochs = {}
        self._lock = asyncio.Lock()

    async def get(self, key):
        async with self._lock:
            if key in self._values:
                return self._values[key]
            task = self._flights.get(key)
            if task is None:
                epoch = self._epochs.get(key, 0)
                task = asyncio.create_task(self._load(key, epoch))
                self._flights[key] = task
        return await asyncio.shield(task)

    async def invalidate(self, key):
        async with self._lock:
            self._epochs[key] = self._epochs.get(key, 0) + 1
            self._values.pop(key, None)
            self._flights.pop(key, None)

    async def _load(self, key, epoch):
        try:
            value = await self._loader(key)
            async with self._lock:
                if self._epochs.get(key, 0) == epoch:
                    self._values[key] = value
            return value
        finally:
            async with self._lock:
                self._flights.pop(key, None)
