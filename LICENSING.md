# Selected licenses and exact scope

Jaime Lawson approved public release of the verified v4 benchmark and selected **CC BY 4.0 for original research documentation** and **MIT for original benchmark scripts**. This v5 copy applies those choices without changing measurements, raw evidence, test logic or third-party terms. Copyright 2026 Jaime Lawson, Phoenix Applied Technologies, for original contributions only.

## Original research documentation: CC BY 4.0

The original narrative in the root reports and publication documents, original appendices under `supporting-evidence/docs/`, original publication README/discussion text, governance notes and original validation explanations is licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). The two PDFs carry the same license for their original report content; embedded fonts keep their own license. The [full license text](licenses/LICENSE-CC-BY-4.0.txt) is included.

Attribution: **Jaime Lawson, Founder & Research Lead, Phoenix Applied Technologies**. Include the license reference and indicate changes when redistributing adaptations. Source links and upstream credits remain applicable. The grant covers only original contributions the licensor owns, not quotations, model-generated excerpts, trademarks, fonts or other third-party material inside a document.

## Original benchmark scripts: MIT

The following two publication tools were created for this research package and are covered by the included [MIT license](licenses/LICENSE-MIT.txt):

* `tools/verify_coding.py` - the original isolated offline fixture runner.
* `supporting-evidence/scripts/rebuild_tables.py` - the original evidence/table verification tool.

The external [file-by-file scope manifest](licenses/LICENSE-SCOPE.csv) supplies their license attribution without editing the preserved script bytes. The MIT grant applies to those scripts, not automatically to code they inspect or execute.

## Preserved material and exclusions

| Material | Treatment |
|---|---|
| Colibri context in `cuda-test-cap.patch` | Existing Apache-2.0 source terms and notices retained; local experimental changes remain clearly identified; no MIT/CC relicensing of the patch |
| DejaVu font subsets in PDFs | Existing font-family terms retained |
| Raw logs, configurations, sampled data and expert-history seeds | Preserved experiment evidence; no blanket new grant over third-party diagnostic text or formats |
| Historical test fixtures, prompts and saved model-generated fixes/transcripts | Preserved as approved benchmark evidence; excluded from the new MIT grant because original authorship/reuse terms are not fully documented |
| Flint weights and Colibri/runtime binaries | Not included; upstream licensing is not changed |

The scope manifest lists exact paths, hashes and treatment for every included file other than the manifest itself and root checksums. It is the controlling scope list for this release; a license choice never expands automatically to third-party content or to future files. The complete 308-file supporting-evidence tree remains byte-identical to v4.

## Specific remaining provenance questions

1. The saved `tests/async-cache/buggy_cache.py` and `test_cache.py` were copied from the local experiment. Its result report says the task was reused from an earlier 176B experiment. The inspected records do not identify an external source or supply an explicit original-authorship/license declaration. The question is who authored that earlier fixture and harness. The embedded copies in prompts share this gap. They are not newly marked MIT.
2. `tests/async-cache/flint_fixed_cache.py`, `q8_fixed_cache.py`, proposed diffs and model conversations contain Flint output and, in the coding files/prompts, the underlying fixture. No external rights holder or conflicting notice was identified in the inspected artifacts, but generated-output copyrightability and any unrecorded third-party source cannot be established solely from the model's Apache-2.0 label. They remain evidence, not an assertion of exclusive ownership or a new reuse license.
3. The immutable base-model revision behind the pinned GGUF was not independently resolved. No weights are distributed, so this is a provenance limitation rather than a missing license for shipped weights.

Jaime's publication authorization and selected licenses are recorded; this list is not a request to repeat that approval. The technical/privacy review passes, but it is not an unconditional legal clearance of every historical or generated artifact. Preserve these qualifications when transferring the package for publication. [Third-party notices](THIRD-PARTY-NOTICES.md) provide the existing terms and upstream sources.

License sources: [Creative Commons official legal text](https://creativecommons.org/licenses/by/4.0/legalcode.txt), [SPDX MIT text](https://raw.githubusercontent.com/spdx/license-list-data/main/text/MIT.txt), and [OSI MIT reference](https://opensource.org/license/mit). The MIT copyright line identifies only the original scripts; upstream copyright lines remain unchanged.
