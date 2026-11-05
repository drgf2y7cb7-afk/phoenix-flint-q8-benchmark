# Quality: successful code repair and a physics failure

Runtime completion and speed do not establish correctness. The grading below uses delivered final answers and pre-existing tests, separately from reasoning length or token rate.

## Async-cache repair

The problem asks for a minimal fix to an asynchronous cache invalidation race: cleanup from an older in-flight load can remove a newer task for the same key. The prompt and grading key were fixed before the original model submission. Seven executable tests check coalescing, cancellation shielding, old success and old failure preserving a newer flight, stale-value protection, retry after failed loading, and concurrent loading of different keys.

| Saved artifact | Result |
|---|---|
| Original buggy implementation | 5 tests pass, 2 fail |
| Completed single-GPU Flint patch | 7 tests pass |
| Later dual-GPU Flint patch | 7 tests pass |

Both fixes add the generation/epoch guard to stale cleanup. The saved model output was a diff fragment without complete file/hunk headers. Formatting and indentation were normalized to apply the exact semantic edit; no new fix logic was added. The later answer's prose regression assertion was vague, but the executable tests enforce the required interleaving.

The original first attempt ended at a 2,048-token ceiling during reasoning, with no final answer. The unchanged question was resubmitted in a fresh conversation at a larger ceiling. Therefore the eventual success is not presented as first-attempt success. The later dual-GPU run revisited the same known problem, and its seven test passes are not seven independent model tasks.

All fixtures, expected baseline failures, model patches, prompt, and grading key are included under [tests/async-cache](../tests/async-cache). Original evidence: [single-GPU test output](../evidence/single-gpu-coding/flint-test-results.txt), [initial truncated export](../evidence/single-gpu-coding/first-attempt-export.json), [dual-GPU test output](../evidence/dual-gpu-coding/q8-test-results.txt), and [dual-GPU grade](../evidence/dual-gpu-coding/q8-grade.json).

The publication audit replayed these saved fixtures offline: the buggy implementation again failed two tests, and both saved patches again passed all seven. This verifies the archived code behavior; it is not a new inference run. [Audit summary](../data/publication-audit.json).

## Five targeted practical answers

The small quality subset reused historically troublesome questions. It contains five answers in three conversations, including two follow-ups. The original assessment records **four practical passes and one failure**; this is a count of this selected set, not an 80% everyday accuracy estimate.

| Case | Recorded grade | Interpretation |
|---|---|---|
| Ice at 0°C in an unpowered insulated cooler | Pass | Correctly describes slower heat entry and eventual melting |
| Longer insulation explanation | **Fail** | Misrepresents GPU thermal-interface materials as barriers that slow heat reaching the cooler |
| One-sentence insulation follow-up | Pass | Correct general summary; does not repair the preceding bad example |
| Hypothetical photo recovery | Pass | Checks backup contents and protects original data; minor imprecision retained |
| Recovery follow-up with newer missing photos | Pass with observation | Avoids promising recovery, but understates uncertainty when calling recovery unlikely |

The recovery prompts are explicitly hypothetical and are reproduced without personal storage locations. [Frozen plan](../evidence/quality-cases/frozen-plan.json), [assessment](../evidence/quality-cases/assessment.json), and [conversation exports](../evidence/quality-cases/insulation-conversation.json) preserve the source evidence. Earlier Lucy responses are not republished or treated as a matched contemporary comparison.

## Known physics failure

The single-GPU insulation answer places GPU thermal pads and interface materials between a hot die and its cooler and says they slow heat reaching the cooling solution. Later full responses repeated variants of the error, including the claim that added insulation in this path lowers component temperature. The original dual-Vulkan answer also reverses the effect of reduced contact resistance.

The practical problem is the application to an internally heat-generating component: thermal interfaces are intended to support heat transfer to the cooler. Intel's primary documentation describes TIM as enabling efficient thermal exchange between a processor and its heatsink. This reference supports the interface distinction; it is not a measurement of Flint's GPU temperatures. [Intel: How to Apply or Remove Thermal Interface Material](https://www.intel.com/content/www/us/en/support/articles/000005576/processors.html).

The reference was checked after generation and was not supplied to Flint. The failure is based on materially misleading hardware explanation, not typography, word count, optional detail, or minor terminology. No hardware action was taken based on the model's answer.

The later temperature-verified 4060 control explicitly cautions against blocking heat from reaching a heatsink but still contains a confusing thermal-pad example. The cache-enabled and Ti-primary answers introduce further conductivity wording problems. Those later responses are discussed qualitatively rather than assigned a new invented aggregate grade. The saved earlier failures remain valid evidence; they do not mean every later response is identical or equally wrong.

Evidence: [single-GPU full answer](../evidence/quality-cases/insulation-conversation.json), [1070 full CUDA assessment](../evidence/thread-cache-1070/accuracy-assessment.json), [1080 Ti full assessment](../evidence/tuned-1080ti/accuracy-observation.json), [later control](../evidence/prefill-cache-1080ti/cache-off-zero-conversation.json), [Ti-primary response](../evidence/gpu-role-1080ti/ti-primary-conversation.json).

## What these tests support

Flint produced a useful fix to one saved concurrency problem and passed its predefined tests. It also produced a substantive physics error despite extensive reasoning and successful runtime completion. Neither result establishes broad coding competence, scientific reliability, or an overall accuracy ranking. A broader evaluation should freeze a diverse unseen task set and grading criteria before model generation.
