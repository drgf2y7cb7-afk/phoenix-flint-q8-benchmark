# Measurement methods

## Scope and run boundaries

The evidence consists of saved experiments from November 4, 2026. The publication audit collected snapshots at 22:22 UTC that day. It performed no inference and did not change production settings. Original reports are retained privately; public evidence files are sanitized copies. Later experiments outside this snapshot are not silently incorporated.

The main timing prompt is preserved in [insulation-0-prompt.txt](../evidence/quality-cases/insulation-0-prompt.txt):

> GPU activity diagnostic 2: Explain how insulation slows heat transfer, using general physical principles in about 250 words. This is a hardware timing check. Do not use tools.

Coding uses a separate, 491-prompt-token async-cache repair problem in [prompt.txt](../tests/async-cache/prompt.txt). The insulation runs report 37 prompt tokens. The exact prompt, response limit, finish status, and generation settings must travel with each rate.

The historical tests used the visible Colibri composer and Send action in fresh conversations, except the explicitly retained follow-up quality questions. JSON exports preserve responses and reasoning. No new hidden API generation was performed for this publication audit.

## Three different timing quantities

| Quantity | Definition and evidence | What it does not mean |
|---|---|---|
| Sampled cumulative decode rate | Last active `live[0].tok_s` from `/health`; paired with its sampled generated-token count | Exact completed-run average, instantaneous speed, or final-answer-only speed |
| Completed decode rate | `completion_tokens / wall_s` from a completed `/profile` turn | End-to-end request throughput or visible words per second |
| Send-to-completion bracket | Recorded Send event to last active sample / first subsequent idle sample | Exact browser-render completion or time to first visible token |
| Prompt phase | Health `read_s`; separate from decode-loop duration | A controlled prompt-prefill microbenchmark, or guaranteed user-visible first-token latency |

The later completed-profile rates are directly reconstructible: `1819 / 59.709215 = 30.464309…`, `1819 / 59.508387 = 30.567120…`, `2164 / 82.845039 = 26.121057…`, and `4569 / 223.770323 = 20.418257…` tok/s. All token counts include reasoning. These are engine-native accounting boundaries; retained logs can count initial/forward tokens differently, especially with Vulkan speculation. Do not replace one accounting method with another without documenting the change.

Most later monitoring slept 0.75 seconds between collection cycles; early monitoring used about two seconds. Network polling, GPU queries, and scheduling add overhead, so the actual observation gaps—not the nominal sleep alone—define the brackets. They are observed bounds, not confidence intervals. A health sample is not a frame-by-frame browser measurement.

The single-GPU coding report provides a 235.938–237.988-second bracket and raw health samples containing the reported 16.259 tok/s observation. A separate machine-readable Send event was not found for that run. Its bracket is retained as recorded rather than represented as independently reconstructed. For quality cases, a field historically labeled `first_token_approx_seconds` is presented here as an approximate prompt-phase observation, not a directly measured visible first token.

## Output limits and run counts

* Initial backend screen: five 256-token capped runs and one full Vulkan response.
* CPU/cache sweep on 4060 + 1070: twelve 768-token screens and one full CUDA response. The 8-thread 5.0 allowance was repeated twice; the final 5.5 allowance twice; most other arms once.
* 80/20 cache experiment on 4060 + 1070: one capped run per backend.
* 1080 Ti transition: one desktop-loaded run, one concurrent-service run, four clean short arms, and one normal full response. The first two are excluded from clean comparisons.
* Prompt-aware cache experiment: one excluded baseline and one valid full response per setting.
* GPU-role experiment: one full response per primary-GPU placement. The 4060 control can also be compared with the previous full-response control.
* Coding: one completed single-GPU response after an earlier 2,048-token truncation, plus one later completed dual-GPU response to the same problem.
* Quality subset: five answers in three conversations; two are follow-ups, not independent samples.

The machine-readable ledger has 40 measured run/case rows, including exclusions. The initial truncated coding attempt is preserved separately but has no comparable verified rate in the ledger. These counts are not 40 independent benchmark tasks.

## Controls and confounders

Fixed prompt and model bytes were preserved. Later arms restarted with separate copies of frozen expert-frequency/heat seeds. This controls the initial seed within those comparisons; it does not make the seed representative of unseen tasks. The insulation question had already been used in prior sessions, so routing history may favor it.

The UI Reasoning checkbox was off in many experiments, yet exported reasoning was present. These are reasoning-enabled measurements in practice. Temperature-zero output can still differ across arithmetic backends and cache placements. An additional UI slider issue means early reports' stated zero values are not all independently verified; see [limitations](LIMITATIONS.md).

Disk/page-cache coldness was not controlled. Startup warmstart seconds are log observations, not cold-start benchmarks. GPU cache population at startup, filesystem cache warmth, and saved expert history are separate concepts.

## Memory and quality

Engine RSS is process resident memory. Device VRAM figures are sampled **total device memory**, including desktop and other allocations. Host available RAM is system-wide. These are not additive model-memory categories, and sampled peaks can miss brief spikes. Historical metrics sometimes span all samples until the next Send, whereas `resources.json` selects active-generation samples; small differences are expected and retained.

Correctness is evaluated from delivered final answers or the saved executable tests. Runtime success, natural stopping, token speed, and quality are separate outcomes. No everyday accuracy percentage, power-efficiency result, long-context claim, or long-term stability certification is derived.
