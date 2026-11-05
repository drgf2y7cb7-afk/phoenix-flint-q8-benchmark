# Third-party material and provenance

This is a scope-specific inventory, not a blanket license for the benchmark package. The [file inventory](validation/third-party-inventory.csv) records paths, hashes, origin, applicable terms and unresolved scope. The original 308-file sanitized evidence tree is retained byte-for-byte.

## Colibri source excerpt and local modification

The release contains one upstream code excerpt as context in [cuda-test-cap.patch](supporting-evidence/evidence/split-8020-1070/cuda-test-cap.patch). It changes `qwen36_tier.c` for the local 80/20 cache experiment with an opt-in `QT_TEST_8020` cap. This is a **locally modified experimental patch**, not an upstream Colibri release or the selected production configuration. The diff itself marks changed lines; this notice identifies the modification without altering the preserved evidence.

The recorded Colibri source revision is `0a5504a1dc64f86fcd0fe7db298b0448c730e7e6`, v2.1.0. Copyright 2026 Vincenzo Fornaro. The source is Apache-2.0. Exact upstream [LICENSE](licenses/colibri/LICENSE), [NOTICE](licenses/colibri/NOTICE) and [THIRD_PARTY_NOTICES.md](licenses/colibri/THIRD_PARTY_NOTICES.md) are included from the saved checkout and hash-checked against it. [Pinned upstream NOTICE](https://github.com/JustVugg/colibri/blob/0a5504a1dc64f86fcd0fe7db298b0448c730e7e6/NOTICE).

The upstream third-party notice describes other Colibri components and references (ds4/ggml, Swiftlet, vLLM, DeepGEMM and CUTLASS). Their source trees, compiled libraries and model weights are **not shipped here**. The notice is retained for attribution context; it does not mean this package redistributes all those dependencies. Build logs and runtime records may contain tool names, flags and software diagnostic text.

## Model, generated outputs and local test material

No Flint weights, GGUF files or full Colibri executables are included. The [pinned Unsloth model-card metadata](https://huggingface.co/unsloth/flint-GGUF/blob/20468edfc38ab43d6914cc88b08cbecb05d0fc62/README.md) declares Apache-2.0 and identifies `RecursiveSI/flint` as the base. [Recursive's model license](https://huggingface.co/RecursiveSI/flint/blob/main/LICENSE) is also Apache-2.0; this latter link is not an immutable base-checkpoint revision.

The evidence contains Flint-generated reasoning, answers and proposed code, together with local prompts, grading keys, fixtures and verification tools prepared during the research with Codex assistance. No external source for the local async-cache fixture is recorded. That absence is not proof of exclusive ownership. The model license labels alone do not establish blanket rights over every generated answer, embedded quotation or local fixture. Jaime has approved publication of the package. The historical fixture authorship and generated-output provenance questions listed in LICENSING.md remain unresolved; no exclusive-ownership claim or new MIT/CC grant is made for these artifacts.

Numerical expert-history seeds are retained as local experiment data. Runtime logs may contain upstream diagnostic strings. Factual measurements and experimental records are distinguished from expressive source material; no blanket transfer of rights in third-party text is asserted.

## PDF fonts and cited references

The two PDFs embed DejaVu Sans, Sans Bold and Sans Mono font subsets. The [DejaVu font-family notice](licenses/fonts/DEJAVU-LICENSE.txt) preserves the Bitstream Vera permission and attribution (Bitstream copyright 2003; DejaVu changes in the public domain). Debian packaging source is not distributed; its separate packaging terms are outside this font-only inventory.

The physics assessment links to and paraphrases an Intel thermal-interface reference in [QUALITY.md](supporting-evidence/docs/QUALITY.md). No Intel article, manual, screenshot or image is bundled. Linked upstream sites and their trademarks retain their own terms. No model logos or third-party promotional graphics are included.

## Selected licenses and remaining questions

Original documentation uses CC BY 4.0 and the two original publication tools use MIT, within the exact [file scope](licenses/LICENSE-SCOPE.csv). All existing upstream notices remain intact. Historical fixture authorship and generated-output provenance are qualified explicitly in [LICENSING.md](LICENSING.md); the new licenses do not cover those excluded artifacts.
