# Hardware, software, caches, and memory

## Recorded system and model

| Item | Evidence-backed description | Qualification |
|---|---|---|
| OS | Debian GNU/Linux 13 | Publication-time inspection reports 13.7; exact per-run OS package inventory was not archived |
| CPU | AMD Ryzen 7 2700X; eight cores, 16 logical CPUs | Eight OpenMP inference workers retained; total process threads include helpers |
| RAM | Health snapshots report 78.49 GiB total | Approximately 78 GiB usable system RAM; not the same as installed DIMM capacity |
| Primary GPU | NVIDIA RTX 4060, nominal 8 GB, CUDA `sm_89` | Logs identify the device; 4060 power readings were unavailable |
| Early second GPU | NVIDIA GTX 1070, nominal 8 GB, `sm_61` | Used for initial backend, thread/cache, and 80/20 stages |
| Later second GPU | NVIDIA GTX 1080 Ti, nominal 11 GB, `sm_61` | Used for automatic cache, prompt-aware cache, GPU-role and later coding stages; desktop shared this GPU |
| Model storage | Model NVMe, GGUF read in place | Exact device/serial details withheld; filesystem-cache state not controlled |
| Model | Flint Q8_0, 42,301,076,928 bytes | About 42.30 GB decimal / 39.40 GiB; native GGUF without requantization |
| Engine | Colibri v2.1.0, `qwen36` | Source commit `0a5504a1dc64f86fcd0fe7db298b0448c730e7e6` |
| CUDA binary | Pascal + Ada targets, `sm_61` and `sm_89` | Recorded SHA-256 `52985a9a11148e1f036e01f27f36f556a8f697d67f5e46b91f4f18fa60becb42` |
| Toolchain | Installation record: CUDA 12.4, GCC 14 for C, GCC 13 for nvcc | Exact patch versions and a complete dual-architecture compiler invocation were not recovered |
| Vulkan build | Isolated build, `VK=1`, Vulkan 1.2 shader target | Build log retained; exact runtime driver and shader compiler version missing |
| Driver/kernel | No authoritative per-run version inventory recovered | The publication execution environment could not query the NVIDIA driver; this is not evidence of a Phoenix hardware failure |

The source checkout was read-only inspected at the reported commit with no tracked modifications. The dual-CUDA binary was freshly hashed during this audit and matched the recorded hash above. This does not prove that every historical executable was rebuilt from that exact source; binary hashes and runtime logs provide the stronger per-artifact identity. No GPU or full-model benchmarks were run in this audit. The [publication environment snapshot](../data/publication-environment.json) is explicitly separate from historical per-run metadata.

The model's recorded pinned revision and verified hash are in [status.json](../evidence/model-validation/status.json). The [header check](../evidence/model-validation/colibri-header-check.txt) reports 49 layers, 256 experts with top-6 routing, 779 tensors, and Q8_0 expert tensors. The engine's generic `bits=4` banner must not be used to relabel this model as Q4.

## Retained CUDA configuration

The following settings describe the saved later CUDA launcher and controlled test snapshots. They are not recommendations for untested hardware.

```text
CUDA_DEVICE_ORDER=PCI_BUS_ID
CUDA_VISIBLE_DEVICES=<RTX_4060_ID>,<GTX_1080_TI_ID>
COLI_CUDA=1
COLI_VULKAN=0
COLI_CUDA_CHAIN=1
COLI_CUDA_CHAIN_MOE=0
COLI_PLACE=lmhead=0,attnproj=0,shexp=0,experts=all
OMP_NUM_THREADS=8
COLI_NO_OMP_TUNE=1
CUDA_EXPERT_GB=auto
Q36_MTP=0
USAGE_SAVE=1
--gpu 0,1 --vram 0 --auto-tier --ctx 8192 --ram 48 --cap 256
--no-tune-profile --ngen 6144
```

The normal saved launcher uses `--temp 1`; the browser can override it. Later paired tests verified UI temperature 0.0. The prior browser setting restored after those tests was 0.7. **Launcher temperature is not proof of effective request temperature.** Full later paired tests also set `COLI_TIMERS=1` and explicitly controlled `QT_PREFILL_REPLAN`; these diagnostic overrides were not part of the retained normal launcher.

The 4060 held all 49 dense/attention-chain layers and the output projection. Both devices held expert caches, while CPU/system RAM remained involved. This is not a whole-layer split and not GPU-only inference. Slots and memory proportions are not workload percentages: expert routing changes per token.

For the earlier 1070 configuration, CUDA `5.5` allowance yielded 1,253 + 1,762 resident expert slots. Automatic 1080 Ti budgets yielded 1,377 + 2,532 in the 31.194 screen, 1,377 + 2,557 in the normal full response, and 1,377 + 2,570 in the later controls. Variation reflects available VRAM, including desktop use.

## Vulkan and saved expert history

The 1070 Vulkan full profile initially used `COLI_VK_TIER_GB=3.0`, `COLI_VK_TIER_HOST_GB=40`, and `COLI_VK_RESERVE2_GB=1.5`, with 640 + 1,749 GPU slots. The subsequent controlled sweep capped the second cache at 1,700. Its 4.0 primary allowance gave 960 + 1,700 slots. On the Ti, the expanded secondary profile gave 960 + 2,688. The exact saved per-arm configurations and non-executable launcher records accompany the logs.

CUDA warmstart logs report all 12,544 expert entries resident in RAM, with a subset also in GPU tiers. The host expert-stage timing includes orchestration and device work; it is not a pure CPU-only benchmark. Zero disk-service time in later completed profiles does not imply zero storage work during startup. Zero attention fields in chained instrumentation do not mean no attention computation occurred.

Frozen expert-frequency history was converted to the CUDA QTH1 heat format, and each controlled arm began from a separate copy. `HEAT_FILE` loads at startup and is saved on graceful exit. `COLI_USAGE` and `COLI_VOCAB_USAGE` are also directed to isolated state. Reusing a mutated working heat file is not equivalent to resetting the same seed.

Only numeric frozen seeds are included: [1070 frequency seed](../evidence/thread-cache-1070/frozen-expert-usage), [1070 CUDA seed](../evidence/thread-cache-1070/frozen-cuda-heat.bin), and [later paired CUDA seed](../evidence/prefill-cache-1080ti/seed-heat.bin). The later seed hash is `38ba9c37134077697b2952b597818cfe961e6c87dadaa659da987817273474ed`. These encode prior routing counts, not weights or prompts. No isolated history-on/history-off ablation was performed; do not attribute the entire improvement to history.

Warmstart observations include 12.7 seconds for the automatic CUDA screen and 13.1 seconds for the normal CUDA full-profile startup, versus 36.8 / 31.1 seconds for the baseline / expanded Vulkan startup. They exclude other initialization and were not controlled cold-disk tests.

## Selected memory observations

| Run | Engine RSS peak (GiB) | Total 4060 VRAM peak (MiB) | Total second-GPU VRAM peak (MiB) | Sampling qualification |
|---|---:|---:|---:|---|
| Single-GPU coding | 40.03 | 6,231 | Not an inference allocation | Saved completed-run resource report |
| 1070 CUDA full response | 40.02 | 6,621 | 6,884 | Sampled peaks; desktop included |
| 1080 Ti automatic CUDA screen | 40.12 | 6,806 | 9,515 | Active-generation samples |
| 1080 Ti normal full response | 40.04 | 7,004 | 9,527 | Active-generation samples |
| 1080 Ti expanded Vulkan screen | 28.88 | 6,196 | 10,106 | Active-generation samples |
| Later 4060-primary full control | 40.14 | 7,004 | 9,531 | Active-generation samples |

The normal Ti full run had 30.74 GiB minimum available RAM in active samples; the broader metrics window reports 30.73 GiB. Both are preserved. Maximum sampled temperatures for that run were 59°C / 54°C. These short observations do not establish sustained thermal stability or energy efficiency.

Sources: [resource records](../evidence/tuned-1080ti/resources.json), [thread/cache peaks](../evidence/thread-cache-1070/resource-peaks.json), [GPU-role resources](../evidence/gpu-role-1080ti/resources.json), [recorded launcher](../evidence/software/start-colibri-flint-q8-cuda-dual.sh.txt).
