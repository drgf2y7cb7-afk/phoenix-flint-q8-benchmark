# Reproducibility instructions

There are two distinct activities: auditing the saved evidence, which requires no model, and repeating inference, which requires an isolated environment and a new run plan. No inference or production configuration change was performed when assembling this draft.

## 1. Audit the saved package offline

From the proposed repository root, using Python 3:

```bash
python3 scripts/rebuild_tables.py --check
```

The script verifies public evidence hashes, reconstructs the sampled rate and completion brackets for the main timing series, recalculates completed-profile rates, checks the repeated control's exported text, and compares regenerated tables. It calls no inference or network endpoint. Running without `--check` regenerates `data/runs.csv`, `data/verification.json`, and `docs/ALL-RUNS.md` from the included evidence.

The manifest records SHA-256 of each original captured artifact and of its sanitized copy. Those hashes differ where redaction occurred. Public hashes verify this package; original hashes permit the owner to verify private provenance. The originals themselves remain intact outside the proposed repository. Desktop screenshots are withheld because they may expose unrelated information.

To re-run the small deterministic coding fixture checks without any model:

```bash
cd tests/async-cache
PYTHONDONTWRITEBYTECODE=1 python3 test_cache.py buggy_cache
PYTHONDONTWRITEBYTECODE=1 python3 test_cache.py flint_fixed_cache
PYTHONDONTWRITEBYTECODE=1 python3 test_cache.py q8_fixed_cache
```

The first command is expected to return nonzero with two failing tests. Each saved model patch should pass all seven. These checks validate the saved code only; they do not regenerate a model answer or replicate inference timing.

## 2. Resolve the environment before inference

Use a separate checkout and separate state directory. Do not point example commands at an existing production installation. Obtain the pinned model artifact and verify its byte count and SHA-256 from the README. No model weights are distributed here.

Record the exact OS/kernel, CPU, RAM, GPU/driver versions, CUDA toolkit, host compilers, Vulkan runtime and shader compiler, Colibri source commit, executable hashes, and browser/UI build. Save the command and effective per-request settings. The historical record is missing some of these versions, so a bit-for-bit reconstruction of the original executable is not promised.

Source reference from the local installation record: [Colibri pinned commit](https://github.com/JustVugg/colibri/tree/0a5504a1dc64f86fcd0fe7db298b0448c730e7e6). Model reference: [Flint pinned revision](https://huggingface.co/unsloth/flint-GGUF/tree/20468edfc38ab43d6914cc88b08cbecb05d0fc62). These identifiers were verified against local evidence; the publication browser could not retrieve the pinned remote pages. Recheck availability before release.

The following single-GPU build invocation is recorded in the original installation, with paths adapted to an isolated checkout:

```bash
make -C colibri/c -j4 qwen36 CUDA=1 CUDA_HOME=/usr \
  NVCC=/usr/bin/nvcc CUDA_ARCH=sm_89 \
  NVCC_PREPEND_FLAGS=-ccbin=/usr/bin/g++-13
```

It does **not** produce the dual-architecture binary needed for the 1070/Ti. The dual build reused Pascal+Ada CUDA objects, and its saved log captures the final host link rather than the full original nvcc command. Recover that command before claiming exact build reproducibility. A prospective rebuild must explicitly include both `compute_61/sm_61` and `compute_89/sm_89`, then verify its cubins and record the full compiler output. This draft does not invent an unverified historical command.

For Vulkan, the local Makefile uses `VK=1`, and the saved build log uses `glslc --target-env=vulkan1.2`. An isolated `make -C colibri/c -j4 qwen36 VK=1` is a reconstruction recipe, not a newly validated build in this audit. Use separate build trees for CUDA and Vulkan. Record toolchain versions and shader outputs.

## 3. Recreate model metadata and test state

The installed CLI's `import` parser supports the following form. Substitute paths under a disposable experiment directory:

```bash
python3 colibri/c/coli import "$MODEL_GGUF" --out "$TEST_MODEL_DIR" --mode link
```

`MODEL_GGUF`, `TEST_MODEL_DIR`, `TEST_ENGINE`, `TEST_STATE_DIR`, `TEST_HOST`, and `TEST_PORT` in this document are placeholders to set explicitly. They are not the owner's production paths or endpoints. Import in link mode reads original model bytes in place; preserve the verified file.

Create fresh state per arm and keep seeds immutable. Direct `COLI_SETUP_HOME`, `COLI_USAGE`, `COLI_VOCAB_USAGE`, `HEAT_FILE`, and cache directories into that arm's state. Copy the same frozen heat file into each working heat path before starting. Later paired runs used the included `seed-heat.bin`; do not substitute a seed from a different stage without recording it. Keep saved expert-history state separate from filesystem/page-cache state.

Inspect and explicitly control relevant process-local `COLI_*`, `QT_*`, `Q36_*`, OpenMP and CUDA variables. The historical launchers cleared inherited tuning variables first. Record GPU enumeration and enforce the intended 4060-first order. Actual UUIDs are intentionally removed from public records; recover your own device identities without assuming numeric order matches Vulkan enumeration.

## 4. Run the planned matched comparison

The saved later CUDA settings are documented in [HARDWARE-AND-CONFIGURATION.md](HARDWARE-AND-CONFIGURATION.md). With those explicit environment values and isolated state, the normalized command shape is:

```bash
python3 colibri/c/coli web --model "$TEST_MODEL_DIR" \
  --gpu 0,1 --vram 0 --auto-tier --ctx 8192 --ram 48 --cap 256 \
  --no-tune-profile --host "$TEST_HOST" --port "$TEST_PORT" \
  --ngen 6144 --temp 0 --model-id flint-q8-test
```

Set `COLI_ENGINE` to the intended verified binary. This is a documented reconstruction, not an executed or validated launch script in the publication package. Historical `.sh.txt` records contain redaction placeholders and are deliberately not runnable. Do not run them as shell scripts.

For the preliminary result, use the exact insulation prompt and a 768-token output ceiling; for complete responses use 6,144. Keep those result categories separate. Verify the visible temperature label after keyboard input and retain the actual request payload if available; changing only a slider DOM value previously failed to update application state. Verify fresh conversation state, context limit, actual emitted reasoning, and the selected backend.

Run no other inference concurrently. Record remaining desktop and background load rather than silently assuming an idle workstation. Do not stop unrelated services as part of an unattended script. A deliberate clean test should be arranged separately from production use.

Before each arm, save seed hashes and effective runtime settings. Preserve startup logs showing device identities, dense-chain placement, expert-slot counts, context, and allocation. Save raw `/health` and GPU samples with timestamps; record Send time; capture completed `/profile` immediately after each full response; export the conversation with finish reason and settings. Preserve failed, truncated, and excluded runs with reasons.

## 5. Proposed independent repetition of 31.2

This is a future protocol, not a claim of tests already completed:

1. Freeze the exact model, binary, prompt, seed, effective temperature, context, token ceiling, and sampling method.
2. Have another operator repeat the same short CUDA configuration. Record whether repetition is on Phoenix or independent hardware.
3. Perform at least three retained runs per arm, resetting the seed each time. Report every observation, range and median; do not publish only the fastest.
4. Separately run full responses with completed-profile timing. Retain prompt phase, decode duration, output length, and end-to-end latency.
5. For cold-versus-warm comparisons, define the policy in advance and document it. The current evidence does not establish a cold-start baseline. Do not flush production caches as part of this draft workflow.
6. Evaluate final-answer correctness independently, using frozen criteria and additional unseen tasks.

Publication may honestly present the existing 31.2 result as preliminary before this repeat, provided the caveat is adjacent to the number. A validated or generally reproducible 31.2 claim requires the additional evidence above.
