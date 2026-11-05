# Draft title

Flint Q8 on Ryzen 2700X + RTX 4060 / GTX 1080 Ti: measurements, cache tuning, and reproducibility limits

# Draft post

We are Phoenix Applied Technologies, working on local AI inference, hardware optimization, offline AI infrastructure, and practical model evaluation. This is our first benchmark report, based on saved Colibri experiments rather than a claim of a general model ranking.

Our later test system runs Debian 13 with a Ryzen 7 2700X, about 78 GiB RAM, an RTX 4060 8 GB, and a GTX 1080 Ti 11 GB. We used Flint Q8_0, a 42,301,076,928-byte GGUF, through Colibri v2.1.0 at commit `0a5504a1dc64f86fcd0fe7db298b0448c730e7e6`. Earlier dual-GPU stages used a GTX 1070 and are labeled separately.

The most useful configuration in these tests kept eight inference CPU workers, the dense CUDA chain on the 4060, and expert caches on both cards with automatic memory allowances. CPU and system RAM remained part of the workload.

The practical comparison is **30.6 tok/s for a complete response to the short explanatory prompt**, versus **20.4 tok/s and about 4:03 total for the coding repair, with 7/7 checks passed**. Both are whole-system measurements with eight CPU inference threads and both GPUs, not standalone 1080 Ti scores. The explanatory test measured speed; it was not an accuracy pass.

| Observation | Rate including reasoning | Measurement |
|---|---:|---|
| Automatic CUDA cache, one 768-token insulation screen | **31.194 tok/s (31.2 rounded)** | **Preliminary** last sampled cumulative decode rate; intentionally truncated |
| Later complete insulation control | 30.464 tok/s | 1,819 completed tokens / 59.709 decode seconds |
| Fresh complete control with identical exported output | 30.567 tok/s | 1,819 completed tokens / 59.508 decode seconds |
| Later complete coding response | 20.418 tok/s | 4,569 completed tokens / 223.770 decode seconds |

The two full controls took about 61–62 and 60–61 seconds from Send to completion. They support repeatability for that question on our machine, but they do not independently repeat the short 31.2 result. The early short screen also has an effective-temperature caveat: a later check found that changing the UI slider's DOM value could leave the application's temperature unchanged. We verified the visible 0.0 label for the later paired full-response tests.

Prompt-aware expert-cache replanning measured 26.121 tok/s versus 30.464 with it off in one matched full-response comparison. Moving the dense primary role to the Ti measured 27.207 versus 30.567 on the 4060. Outputs and automatic cache counts differed slightly, so these are workload-specific observations.

We kept answer quality separate from performance. Flint's async-cache race fix passed all seven saved executable tests, both in the completed single-GPU test and a later repeat of the same problem. An earlier attempt was truncated during reasoning. The insulation question also exposed a material physics error: several responses described GPU thermal-interface materials as barriers that improve cooling by slowing heat flow toward the cooler. The report includes that failure and makes no broad accuracy claim.

The draft package contains a chronological comparison, per-run CSV, sanitized raw logs and conversation exports, model and binary identities, frozen numeric expert-history seeds, offline verification code, and reproduction instructions. It identifies missing driver/toolchain details, uncontrolled filesystem-cache state, changing output length, and excluded background-load runs.

We would welcome feedback on the measurement boundaries and a reproducible method for independently repeating the 31.2 short screen. Our next validation should retain all repeated runs, verify effective request settings, and include fresh unseen workloads.

**Publication editor note:** add the approved repository URL here only after owner approval and repository creation. This file is draft text; it has not been posted.
