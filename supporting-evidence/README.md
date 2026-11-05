# Flint Q8 on Phoenix: local inference measurements

**Phoenix Applied Technologies** · Local AI inference, hardware optimization, offline AI infrastructure, and practical model evaluation

**Private publication draft — November 4, 2026. Owner approval required before release.**

This report follows Flint Q8 from a working single-RTX-4060 configuration to dual-GPU CUDA and Vulkan configurations in Colibri. It publishes observed results, the boundaries of each measurement, and the evidence needed to audit them. These are experiments on one workstation and a small set of prompts, not a standardized model leaderboard.

The current-hardware experiments used a Ryzen 7 2700X, approximately 78 GiB of system RAM, an RTX 4060 8 GB, and a GTX 1080 Ti 11 GB, running Debian 13. **Earlier dual-GPU experiments used a GTX 1070 8 GB instead of the 1080 Ti.** Those stages are explicitly separated below.

The useful practical distinction is **30.6 tokens/sec on the short explanatory input prompt, with a complete response**, versus **20.4 tokens/sec and about 4:03 total on the coding repair**, whose fix passed 7/7 checks. Both rates include reasoning and measure the **whole CPU-and-two-GPU system with eight inference workers**. They are not standalone 1080 Ti scores. The explanatory response was a speed measurement, not an accuracy pass.

## Main findings

* **31.2 tokens/sec remains preliminary.** The underlying observation was **31.194 tok/s**, the last sampled cumulative decode rate during one deliberately capped, 768-token CUDA run. It ended during reasoning, without a final answer. The same short-run result has not been independently repeated, and its intended temperature-zero setting has an unresolved UI verification caveat.
* Two later, complete insulation responses measured **30.464 and 30.567 tok/s**, using completed token counts divided by engine decode-loop time. Both generated 1,819 tokens including reasoning, with identical exported final text and reasoning. These are two same-machine controls on one prompt; they do not independently validate the 31.2 short-screen result.
* The selected configuration kept eight inference CPU workers, the dense computation on the RTX 4060, and expert caches on both GPUs with automatic CUDA memory allowances. CPU and system RAM remain important parts of inference.
* Performance did not establish correctness. A Python async-cache repair passed all seven saved tests, while a thermal-insulation answer gave a materially misleading GPU cooling explanation. Both outcomes are retained.

## Selected comparison

All rates include reasoning tokens. `Sampled` means the last active cumulative `/health` average, which can omit the tail of generation. `Completed` means the completed `/profile` token count divided by its decode-loop duration. End-to-end brackets include prompt processing and UI dispatch; they are not pure decode time.

| Hardware / configuration | Workload and length | Rate (tok/s) | Rate method | Send-to-completion (s) | Interpretation |
|---|---|---:|---|---:|---|
| RTX 4060, CUDA | Async-cache repair, full answer | 16.259 | Sampled | 235.94–237.99 | Seven saved tests passed; followed an initial truncated attempt |
| RTX 4060, CUDA | Insulation, full answer | 16.171 | Sampled | 213.85–215.85 | Known physics failure |
| 4060 + **1070**, Vulkan | Insulation, full answer | 17.691 | Sampled | 76.94–78.98 | Shorter reasoning, not a proportional hardware speedup |
| 4060 + **1070**, tuned CUDA | Insulation, full answer | 25.279 | Sampled | 87.61–88.40 | Faster decode; longer answer than the Vulkan run |
| 4060 + **1080 Ti**, automatic CUDA cache | Insulation, 768-token screen | **31.194** | Sampled | 25.24–26.03 | **Preliminary, one capped run; temperature caveat** |
| 4060 + **1080 Ti**, normal CUDA profile | Insulation, full answer | 30.663 | Sampled | 72.23–73.02 | Natural completion; physics failure retained |
| 4060 + **1080 Ti**, CUDA control | Insulation, full answer, 1,819 tokens | 30.464 | Completed | 61.15–61.94 | Verified visible temperature 0.0 |
| Same hardware, fresh CUDA control | Same full answer, 1,819 tokens | 30.567 | Completed | 60.14–60.94 | Identical exported answer and reasoning |
| 4060 + **1080 Ti**, CUDA | Async-cache repair, full answer, 4,569 tokens | 20.418 | Completed | 242.71–243.50 | Seven saved tests passed; different workload |

Sources: [complete run ledger](docs/ALL-RUNS.md), [machine-readable runs](data/runs.csv), [results and evidence map](docs/RESULTS.md). Do not calculate a hardware-only speedup across these rows: prompt lengths, output lengths, GPU hardware, cache history, sampling settings, and measurement methods differ.

## Model and runtime identity

* Model artifact: `unsloth/flint-GGUF`, `flint-Q8_0.gguf`, revision `20468edfc38ab43d6914cc88b08cbecb05d0fc62`.
* Size: **42,301,076,928 bytes** (42.30 GB decimal; about 39.40 GiB).
* Recorded verified SHA-256: `5df42b56859c7b5142228005d7d63c327ec9e34c99c72548016d805309a0d284`.
* Colibri: **v2.1.0**, source commit `0a5504a1dc64f86fcd0fe7db298b0448c730e7e6`, `qwen36` engine. The dual-CUDA binary targets `sm_61` and `sm_89`.

The file hash was verified by the original download workflow. This publication audit did not rehash all 42.3 GB or run new inference. [Recorded validation](evidence/model-validation/status.json) and [native GGUF header check](evidence/model-validation/colibri-header-check.txt) are included.

## Read and reproduce

1. [Measurement methods](docs/METHODS.md): decode, prompt processing, latency, and uncertainty.
2. [Results](docs/RESULTS.md): progression, tuning sweeps, cache allocation, and exclusions.
3. [Hardware and configuration](docs/HARDWARE-AND-CONFIGURATION.md): versions, settings, seeds, and memory.
4. [Quality evaluation](docs/QUALITY.md): executable coding checks and the physics failure.
5. [Reproducibility instructions](docs/REPRODUCIBILITY.md): offline audit now; proposed isolated inference protocol for later approval.
6. [Limitations and release checklist](docs/LIMITATIONS.md): missing metadata and claims that remain unsupported.
7. [Colibri Discussions draft](DISCUSSION-DRAFT.md).

```bash
python3 scripts/rebuild_tables.py --check
```

This audits saved evidence without invoking a model. The proposed repository structure is the contents of this `public/` directory. [Evidence manifest](data/evidence-manifest.csv) entries distinguish original snapshot hashes from sanitized-copy hashes. No weights, desktop screenshots, private source paths, credentials, or real network endpoints are included. Licensing and release approval remain owner decisions; no license grant is implied by this draft.
