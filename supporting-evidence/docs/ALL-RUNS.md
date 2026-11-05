# Complete run ledger

Rates include reasoning. Sampled health rates are not exact completed-run rates. See METHODS.md for timing boundaries and LIMITATIONS.md for temperature and cache caveats. Each row is one recorded run or case; no aggregate accuracy is implied.

| Run | GPUs | Backend | Type | tok/s | Complete/send bracket (s) | Status |
|---|---|---|---|---:|---:|---|
| `single-gpu-coding/completed` | RTX 4060 only | CUDA | full response | 16.259 | 235.94–237.99 | repeated prompt after initial 2048-token truncation; send timestamp not found as separate event |
| `early-backends-1070/cuda-baseline` | RTX 4060 only | CUDA | short screen | 17.410 | 19.38–21.45 | observed; workload-specific |
| `early-backends-1070/cuda-dual` | RTX 4060 + GTX 1070 | CUDA | short screen | 17.811 | 14.53–16.57 | observed; workload-specific |
| `early-backends-1070/vulkan` | RTX 4060 only | Vulkan | short screen | 15.613 | 22.75–24.79 | observed; workload-specific |
| `early-backends-1070/vulkan-dual` | RTX 4060 + GTX 1070 | Vulkan | short screen | 20.862 | 16.84–18.88 | observed; workload-specific |
| `early-backends-1070/cuda-dual-tuned` | RTX 4060 + GTX 1070 | CUDA | short screen | 16.655 | 17.08–19.12 | observed; workload-specific |
| `early-backends-1070/vulkan-dual-full` | RTX 4060 + GTX 1070 | Vulkan | full response | 17.691 | 76.94–78.98 | observed; workload-specific |
| `thread-cache-1070/t8-v3-r1` | RTX 4060 + GTX 1070 | Vulkan | short screen | 20.483 | 38.41–39.20 | observed; workload-specific |
| `thread-cache-1070/t4-v3-r1` | RTX 4060 + GTX 1070 | Vulkan | short screen | 18.804 | 41.72–42.51 | observed; workload-specific |
| `thread-cache-1070/t6-v3-r1` | RTX 4060 + GTX 1070 | Vulkan | short screen | 19.758 | 39.55–40.34 | observed; workload-specific |
| `thread-cache-1070/t8-v3-r2` | RTX 4060 + GTX 1070 | Vulkan | short screen | 19.633 | 39.87–40.66 | observed; workload-specific |
| `thread-cache-1070/t8-v35-r1` | RTX 4060 + GTX 1070 | Vulkan | short screen | 19.488 | 40.37–41.16 | observed; workload-specific |
| `thread-cache-1070/t8-v4-r1` | RTX 4060 + GTX 1070 | Vulkan | short screen | 21.239 | 36.69–37.48 | observed; workload-specific |
| `thread-cache-1070/c8-v5-r1` | RTX 4060 + GTX 1070 | CUDA | short screen | 26.361 | 30.06–30.84 | observed; workload-specific |
| `thread-cache-1070/c4-v5-r1` | RTX 4060 + GTX 1070 | CUDA | short screen | 25.122 | 31.29–32.08 | observed; workload-specific |
| `thread-cache-1070/c6-v5-r1` | RTX 4060 + GTX 1070 | CUDA | short screen | 25.363 | 31.37–32.15 | observed; workload-specific |
| `thread-cache-1070/c8-v5-r2` | RTX 4060 + GTX 1070 | CUDA | short screen | 25.353 | 31.22–32.02 | observed; workload-specific |
| `thread-cache-1070/c8-v55-r1` | RTX 4060 + GTX 1070 | CUDA | short screen | 27.068 | 29.68–30.47 | observed; workload-specific |
| `thread-cache-1070/c8-v55-r2` | RTX 4060 + GTX 1070 | CUDA | short screen | 26.710 | 29.84–30.63 | observed; workload-specific |
| `thread-cache-1070/cuda-final-full` | RTX 4060 + GTX 1070 | CUDA | full response | 25.279 | 87.61–88.40 | observed; workload-specific |
| `split-8020-1070/vulkan-8020` | RTX 4060 + GTX 1070 | Vulkan | short screen | 19.126 | 41.41–42.20 | observed; workload-specific |
| `split-8020-1070/cuda-8020` | RTX 4060 + GTX 1070 | CUDA | short screen | 21.896 | 37.01–37.80 | observed; workload-specific |
| `initial-1080ti/cuda-matched` | RTX 4060 + GTX 1080 Ti | CUDA | short screen | 13.826 | 58.13–58.92 | excluded from clean comparison: desktop GPU load |
| `tuned-1080ti/cuda-matched` | RTX 4060 + GTX 1080 Ti | CUDA | short screen | 25.709 | 30.38–31.18 | excluded from clean comparison: concurrent 176B service |
| `tuned-1080ti/cuda-clean` | RTX 4060 + GTX 1080 Ti | CUDA | short screen | 27.830 | 28.39–29.18 | observed; workload-specific |
| `tuned-1080ti/cuda-auto` | RTX 4060 + GTX 1080 Ti | CUDA | short screen | 31.194 | 25.24–26.03 | preliminary; unrepeated short screen |
| `tuned-1080ti/vulkan-matched` | RTX 4060 + GTX 1080 Ti | Vulkan | short screen | 20.574 | 38.30–39.08 | observed; workload-specific |
| `tuned-1080ti/vulkan-expanded` | RTX 4060 + GTX 1080 Ti | Vulkan | short screen | 23.378 | 33.20–33.99 | observed; workload-specific |
| `tuned-1080ti/cuda-production` | RTX 4060 + GTX 1080 Ti | CUDA | full response | 30.663 | 72.23–73.02 | observed; workload-specific |
| `prefill-cache-1080ti/cache-off` | RTX 4060 + GTX 1080 Ti | CUDA | full response | 28.873 | 48.70–49.49 | excluded from matched comparison: UI temperature remained 0.7 |
| `prefill-cache-1080ti/cache-on` | RTX 4060 + GTX 1080 Ti | CUDA | full response | 26.121 | 84.60–85.39 | observed; workload-specific |
| `prefill-cache-1080ti/cache-off-zero` | RTX 4060 + GTX 1080 Ti | CUDA | full response | 30.464 | 61.15–61.94 | observed; workload-specific |
| `gpu-role-1080ti/ti-primary` | RTX 4060 + GTX 1080 Ti | CUDA | full response | 27.207 | 53.39–54.18 | observed; workload-specific |
| `gpu-role-1080ti/4060-primary` | RTX 4060 + GTX 1080 Ti | CUDA | full response | 30.567 | 60.14–60.94 | observed; workload-specific |
| `dual-gpu-coding/q8` | RTX 4060 + GTX 1080 Ti | CUDA | full response | 20.418 | 242.71–243.50 | observed; workload-specific |
| `quality-cases/new-cold-object/0` | RTX 4060 only | CUDA | full response | 15.795 | 23.09–25.09 | targeted quality case; follow-ups not independent |
| `quality-cases/insulation/0` | RTX 4060 only | CUDA | full response | 16.171 | 213.85–215.85 | targeted quality case; follow-ups not independent |
| `quality-cases/insulation/1` | RTX 4060 only | CUDA | full response | 14.355 | 12.14–14.14 | targeted quality case; follow-ups not independent |
| `quality-cases/backup-recovery/0` | RTX 4060 only | CUDA | full response | 16.286 | 241.91–243.91 | targeted quality case; follow-ups not independent |
| `quality-cases/backup-recovery/1` | RTX 4060 only | CUDA | full response | 15.973 | 151.80–153.81 | targeted quality case; follow-ups not independent |

CSV with token counts, prompt timings, measurement methods and evidence paths: [runs.csv](../data/runs.csv).
