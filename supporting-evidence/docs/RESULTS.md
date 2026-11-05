# Results and progression

This is a chronological engineering record. A later stage changes more than one condition unless explicitly stated. The complete [run ledger](ALL-RUNS.md) and [CSV](../data/runs.csv) retain individual observations, including excluded runs.

## 1. Working single-GPU baseline

The RTX 4060-only CUDA profile used eight OpenMP workers, an 8,192-token context, a 6,144-token full-response ceiling, and system RAM for the expert working set. The completed async-cache repair was sampled at 16.259 tok/s and took 235.94–237.99 seconds, including 6.174 seconds of prompt processing. It passed the seven fixed tests after an initial attempt exhausted a 2,048-token ceiling during reasoning.

The separate insulation response was sampled at 16.171 tok/s and took 213.85–215.85 seconds. It failed the practical correctness criterion. Neither figure is a completed-profile average.

Evidence: [coding result](../evidence/single-gpu-coding/results.json), [coding raw samples](../evidence/single-gpu-coding/final-resource-samples.jsonl), [quality metrics](../evidence/quality-cases/metrics.json).

## 2. Initial CUDA/Vulkan exploration with GTX 1070

The second inference GPU at this stage was a GTX 1070, not a 1080 Ti. Five 256-token screens yielded 17.410 tok/s for single-GPU CUDA, 17.811 for dual CUDA, 15.613 for single-GPU Vulkan, 20.862 for dual Vulkan, and 16.655 for a CUDA scheduling/binding variation. Their intended temperature was zero, subject to the later UI caveat.

A full Vulkan response measured 17.691 tok/s, with a 76.94–78.98-second completion bracket. It produced substantially less reasoning than the earlier single-GPU answer. The shorter total latency therefore cannot be described as a 2.7× hardware speedup. Its final answer also failed the physics check.

Evidence: [metrics](../evidence/early-backends-1070/metrics.json), [full conversation](../evidence/early-backends-1070/vulkan-dual-full-conversation.json), [assessment](../evidence/early-backends-1070/assessment.json).

## 3. Thread and cache sweep with GTX 1070

All short runs were capped at 768 tokens, with copies of frozen expert history. The following rates are sampled cumulative averages.

| Backend | Inference threads | Recorded allowance | Repetitions / rates (tok/s) |
|---|---:|---|---|
| Vulkan | 4 | 3.0 primary tier | 1: 18.804 |
| Vulkan | 6 | 3.0 primary tier | 1: 19.758 |
| Vulkan | 8 | 3.0 primary tier | 2: 20.483, 19.633 |
| Vulkan | 8 | 3.5 primary tier | 1: 19.488 |
| Vulkan | 8 | 4.0 primary tier | 1: 21.239 |
| CUDA | 4 | 5.0 per-device allowance | 1: 25.122 |
| CUDA | 6 | 5.0 per-device allowance | 1: 25.363 |
| CUDA | 8 | 5.0 per-device allowance | 2: 26.361, 25.353 |
| CUDA | 8 | 5.5 per-device allowance | 2: 27.068, 26.710 |

Eight workers were retained. The six-versus-eight difference at the same allowance is small relative to observed variation; this is not strong evidence of an eight-thread optimum. The two CUDA 5.5 observations average 26.889 tok/s, versus 25.857 for the two 5.0 observations, about 4% higher in this screen. CUDA and Vulkan allowance fields have different semantics and should not be equated with identical memory allocations.

The full CUDA response was sampled at 25.279 tok/s and finished in 87.61–88.40 seconds. Despite faster decode than the preceding Vulkan response, its total latency was longer because it generated more reasoning. It failed the practical physics criterion.

Evidence: [metrics](../evidence/thread-cache-1070/metrics.json), [protocol](../evidence/thread-cache-1070/protocol.json), [CUDA startup](../evidence/thread-cache-1070/c8-v55-r1.log), [full response](../evidence/thread-cache-1070/cuda-final-full-conversation.json).

## 4. Reduced 80/20 expert-cache allocation

On 4060 + 1070, Vulkan's GPU cache was reduced from 960 + 1,700 slots to 960 + 240; CUDA's from 1,253 + 1,762 to 1,253 + 313. This was a ratio of resident expert slots, not a whole-model split or percentage of GPU computation.

One capped run per backend measured 19.126 tok/s for Vulkan and 21.896 for CUDA. Both were lower than their earlier tuned screens. Total GPU-resident capacity fell sharply, so the experiment does not isolate scheduling balance at fixed capacity. The CUDA arm used a separate opt-in experimental source patch; that result must not be attributed to the stock production binary.

Evidence: [metrics](../evidence/split-8020-1070/metrics.json), [CUDA patch](../evidence/split-8020-1070/cuda-test-cap.patch), [Vulkan log](../evidence/split-8020-1070/vulkan-8020.log), [CUDA log](../evidence/split-8020-1070/cuda-8020.log).

## 5. GTX 1080 Ti and automatic cache budgets

The clean short-screen series used 4060 + 1080 Ti. Each arm was run once.

| Configuration | GPU expert slots: 4060 + Ti | Sampled tok/s | Send-to-completion (s) | Peak engine RSS (GiB) |
|---|---:|---:|---:|---:|
| Fixed-budget CUDA | 1,253 + 1,762 | 27.830 | 28.39–29.18 | 39.96 |
| Automatic-budget CUDA | 1,377 + 2,532 | **31.194** | 25.24–26.03 | 40.12 |
| Vulkan baseline | 960 + 1,700 | 20.574 | 38.30–39.08 | 32.12 |
| Expanded Vulkan secondary cache | 960 + 2,688 | 23.378 | 33.20–33.99 | 28.88 |

The 31.194 observation rounds to 31.2. It is **preliminary**, capped during reasoning, unrepeated under the same short-run protocol, and subject to the unresolved early UI-temperature caveat. The nominal 12.1% difference from fixed CUDA and 33.4% difference from expanded Vulkan describe these observations only, not a general backend ranking.

The normal full response then measured 30.663 tok/s by its last live sample, with a 72.23–73.02-second bracket and natural completion. It retained the misleading GPU-insulation explanation. Automatic expert counts differed slightly (1,377 + 2,557) because free VRAM changed.

Two transition runs are preserved but excluded from this clean comparison: a 13.826 tok/s run with heavy desktop GPU load, and a 25.709 tok/s run while a separate 176B service occupied resources. These observations cannot isolate the effect of replacing the 1070.

Evidence: [clean-series metrics](../evidence/tuned-1080ti/metrics.json), [active resource samples](../evidence/tuned-1080ti/resources.json), [31.194 startup/log](../evidence/tuned-1080ti/cuda-auto.log), [raw timing samples](../evidence/tuned-1080ti/samples.jsonl), [physics assessment](../evidence/tuned-1080ti/accuracy-observation.json), [loaded desktop run](../evidence/initial-1080ti/metrics.json).

## 6. Later full-response controls

| Comparison arm | Completed tokens | Decode-loop seconds | Completed tok/s | Prompt seconds | Send-to-completion (s) |
|---|---:|---:|---:|---:|---:|
| Prompt-aware cache replanning off | 1,819 | 59.709215 | 30.464 | 1.065 | 61.15–61.94 |
| Prompt-aware cache replanning on | 2,164 | 82.845039 | 26.121 | 1.838 | 84.60–85.39 |
| Fresh 4060-primary control | 1,819 | 59.508387 | 30.567 | 1.077 | 60.14–60.94 |
| 1080 Ti as dense-compute primary | 1,437 | 52.818243 | 27.207 | 1.030 | 53.39–54.18 |

The valid cache on/off pair and the GPU-role pair verified the visible temperature label at 0.0. Cache replanning was about 14.26% slower in this one comparison; its longer output also increased total latency. The Ti-primary run was about 10.99% slower in decode rate than the fresh 4060 control, despite finishing earlier with fewer tokens. These results supported retaining the 4060 primary and leaving prompt-aware cache replanning off for this setup.

The two 4060 baseline responses have identical exported final text and reasoning. Their completed rates differ by about 0.34%, supporting repeatability on that question. They are same-machine observations, not an independent replication by another operator or system. Automatic expert slots differed slightly between arms; output arithmetic can differ even at temperature zero.

Evidence: [cache comparison](../evidence/prefill-cache-1080ti/comparison.json), [GPU-role comparison](../evidence/gpu-role-1080ti/comparison.json), [matching-output record](../evidence/gpu-role-1080ti/prior-control-comparison.json).

## 7. Later coding response

The later dual-GPU Q8 coding arm completed 4,569 tokens in 223.770323 decode seconds: **20.418 tok/s**, plus a 19.278-second prompt phase. The send-to-completion bracket was 242.71–243.50 seconds. All seven saved tests passed again. This is a repeat of the same repair problem, not a second independent coding benchmark.

This Q8 arm came from an ongoing Q6-versus-Q8 experiment. Only the completed Q8 artifacts are included; no Q6 result or quantization comparison is claimed. Evidence: [completed profile](../evidence/dual-gpu-coding/q8-profile.json), [metrics](../evidence/dual-gpu-coding/metrics.json), [grade](../evidence/dual-gpu-coding/q8-grade.json), [test output](../evidence/dual-gpu-coding/q8-test-results.txt).
