# Flint Q8 Benchmark

**Jaime Lawson** | Founder & Research Lead, **Phoenix Applied Technologies**

**Public benchmark contact:** [jmlawson@outlook.com](mailto:jmlawson@outlook.com)

Local AI inference, hardware optimization, offline AI infrastructure and practical model evaluation.

**Release package v5 - November 5, 2026. Publicly available on GitHub.**

## System and model

Debian 13; AMD Ryzen 7 2700X; approximately 78 GiB RAM; RTX 4060 8 GB + GTX 1080 Ti 11 GB. Flint Q8_0: **42.30 GB**; Colibri v2.1.0. Later CUDA tests used eight inference CPU workers, dense computation on the 4060, and expert caches on both GPUs. These are whole-system results, including CPU/RAM, not standalone GPU scores.

## Results at a glance

All rates include reasoning. Completed rates use final token counts / decode-loop time; sampled rates are the last active cumulative average.

| Test | Decode rate | End-to-end time | Evidence status |
|---|---:|---:|---|
| Full explanatory response, control A | 30.464 tok/s | 61.15-61.94 s | Completed; 1,819 tokens |
| Full explanatory response, control B | **30.567 tok/s** | 60.14-60.94 s | Completed; same 1,819-token output |
| Full coding repair | **20.418 tok/s** | **242.71-243.50 s** | Completed; fix passed 7/7 tests |
| 768-token explanatory screen | **31.194 tok/s** | 25.24-26.03 s | **Preliminary** sampled rate; truncated |

The two explanatory controls verified similar performance on the same machine and prompt, with identical exported final text and reasoning. They are not independent replications. **31.2 tok/s remains preliminary:** one capped run, no same-protocol independent repeat, and an unresolved early UI-temperature caveat. Sources: [E1-E4 in the technical report](TECHNICAL-REPORT.md#evidence-key).

## Optimization and correctness

Automatic CUDA cache allocation measured 31.194 versus 27.830 tok/s with a fixed allowance in the short screen, a **12.1% observed increase**, subject to the same preliminary caveat. On later full responses, prompt-aware cache replanning was **14.3% slower**, and moving dense computation to the Ti was **11.0% slower**. These are workload-specific observations; faster decode did not always mean a shorter answer.

The async-cache repair passed seven predefined checks in both saved completed attempts. The first single-GPU attempt had truncated before a final answer. The baseline code fails two tests. **The physics failure remains documented:** several insulation responses misrepresented GPU thermal-interface materials as barriers that improve cooling by slowing heat toward the cooler. The explanatory timing test was not an accuracy pass. No general coding or accuracy score is claimed.

## Evidence and credits

The four-page technical report, raw evidence and verified offline test commands accompany this summary. Credit: Colibri developers, including Vincenzo Fornaro; Recursive for Flint; Unsloth for GGUF packaging. Codex/Sapphire assisted preparation and verification; this is not independent replication. See CREDITS.md and LICENSING.md for attribution and license scope.

Original research documentation: Copyright 2026 Jaime Lawson, Phoenix Applied Technologies. Licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/); third-party material excluded. See LICENSING.md.
