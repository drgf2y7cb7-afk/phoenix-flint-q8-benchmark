# Limitations, conflicts, and publication review

## Claims that remain limited

* **31.2 tok/s:** one 768-token screen, intentionally truncated during reasoning, with last sampled rate 31.194. No same-protocol independent repeat is present. Later 30.464/30.567 full responses are separate observations.
* **Temperature:** an early UI method changed the range input's DOM value without updating the application state. The excluded first cache-off run remained at a visible 0.7. Earlier reports' stated zero settings are therefore recorded as intended/reported unless independently verified. The valid later cache pair and GPU-role pair used keyboard input and visible 0.0 verification. The effective early request payloads were not recovered.
* **Hardware progression:** early dual runs used a GTX 1070. The 1080 Ti series also changed desktop placement and cache budgets. There is no isolated hardware-swap speedup result.
* **Workload selection:** one insulation prompt dominates timing. Expert history already included related usage. Coding results repeat one problem, and five practical answers form a failure-selected subset with follow-ups. No broad accuracy percentage or general throughput is established.
* **Caching:** initial cold/default expert ordering differed from seeded later runs. No isolated history ablation was done. Filesystem/page-cache coldness was not controlled. Automatic memory budgets vary with free VRAM.
* **Measurement boundaries:** old rates are last sampled cumulative averages; later rates use completed profiles. Output lengths differ. End-to-end brackets are sampled, not millisecond-precise browser timings. Initial coding Send time was not found as a separate machine-readable event.
* **Memory and thermals:** VRAM includes desktop use; peak sampling can miss spikes. RSS and system available RAM have different scopes. No long-context stress test, sustained thermal soak, complete energy measurement, or long-term reliability certification is included.
* **Version completeness:** driver, kernel and exact compiler/runtime patch versions are not pinned per historical run. The complete original dual-CUDA compile command was not recovered. Exact binary regeneration is therefore incomplete.
* **Remote references:** pinned source/model identities are supported by local artifacts; their remote pages could not be retrieved during this audit. Intel's TIM reference was successfully checked.
* **Ongoing work:** the later coding Q8 arm was captured from an active Q6/Q8 experiment. The Q8 answer and its tests were complete. There is no Q6 result in this report and no claim that other work stopped.

## Resolved discrepancies

| Apparent conflict | Resolution |
|---|---|
| 31.2 versus 30.5 versus 20.4 tok/s | Different output limits, prompts, sampling settings, and rate definitions; retain separate rows |
| Faster CUDA took longer than Vulkan | CUDA generated more reasoning in those full-response runs |
| 1080 Ti primary finished sooner | It generated 382 fewer tokens; its decode rate was lower |
| 13.826 or 25.709 tok/s transition observations | Retained as excluded desktop-loaded/concurrent-service runs |
| `metrics.json` and `resources.json` RAM minima differ slightly | Broad Send-to-next-Send window versus active-generation window; do not overwrite either |
| Source banner says `bits=4` | Native header validation identifies Q8_0 expert weights; generic banner is not the GGUF quantization label |
| Reasoning checkbox is off | Reasoning exists in exports; measurements include it |
| A saved report says a server is running | Historical status at that experiment's conclusion, not current status established by this audit |

The public dataset contains original measured numbers with redactions; it does not silently repair historical claims. Curated narrative and table status fields carry the interpretation and exclusions.

## Proposed repository layout

```text
README.md
DISCUSSION-DRAFT.md
docs/
  RESULTS.md
  ALL-RUNS.md
  METHODS.md
  HARDWARE-AND-CONFIGURATION.md
  QUALITY.md
  REPRODUCIBILITY.md
  LIMITATIONS.md
data/
  runs.csv
  evidence-manifest.csv
  verification.json
evidence/
  single-gpu-coding/
  quality-cases/
  early-backends-1070/
  thread-cache-1070/
  split-8020-1070/
  initial-1080ti/
  tuned-1080ti/
  prefill-cache-1080ti/
  gpu-role-1080ti/
  dual-gpu-coding/
  model-validation/
  software/
scripts/rebuild_tables.py
tests/async-cache/
SHA256SUMS
```

The owner's private provenance map, original snapshots and audit working files remain outside this tree and outside the distribution ZIP. No model weights or executable engine binaries are included.

## Before any public release

1. Obtain the owner's explicit approval of this exact package and publication text.
2. Review the sanitization report and selected transcripts. Confirm that all content is intended for public release.
3. Decide a repository name, contact policy, and license for original report/test material. Review upstream terms before choosing a license; this draft grants none.
4. Confirm the missing version/build metadata, or keep the limitations conspicuous. Recheck pinned source/model links.
5. Either independently repeat the preliminary 31.2 result or preserve its preliminary designation in every headline and table.
6. Run the offline hash/table check on the final approved bytes. Keep exclusions, code failures, physics failure and provenance relationships intact.

No repository has been created, no upload or public message has been sent, and no publication is authorized by preparing this draft.
