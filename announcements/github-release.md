# Draft GitHub release

**Proposed version:** `v5.0`. Prepared for owner review only; no tag, Release or release asset has been published.

**Title:** Flint Q8 on a mixed-generation dual-GPU workstation

**Author:** Jaime Lawson, Founder & Research Lead, Phoenix Applied Technologies.

This benchmark documents Flint Q8_0 (42.30 GB) through Colibri on Debian 13, a Ryzen 7 2700X, approximately 78 GiB RAM, RTX 4060 8 GB and GTX 1080 Ti 11 GB. Eight CPU inference workers and both GPUs contribute to the later whole-system results.

Completed explanatory responses measured 30.464 and 30.567 tokens/s on the same prompt and machine, with identical exported final text and reasoning. A harder coding repair measured 20.418 tokens/s and about 4:03 total; its saved fix passes 7/7 predefined tests. Rates include reasoning. The separate capped 31.194 tokens/s screen (31.2 rounded) remains preliminary and has not been independently repeated under the same protocol.

The report distinguishes decode rate, end-to-end latency and correctness. It retains the failed physics explanation, the baseline's two coding-test failures, incomplete attempts and reproduction limits. The small task set does not establish general accuracy or coding capability.

The repository contains a one-page summary, four-page technical report, unchanged sanitized evidence and verified offline test commands. Credit to Colibri's developers including Vincenzo Fornaro, Recursive and Unsloth. Codex/Sapphire assisted preparation and verification; these checks are not independent benchmark replication.

**Public benchmark contact:** [jmlawson@outlook.com](mailto:jmlawson@outlook.com)

[Repository](https://github.com/drgf2y7cb7-afk/phoenix-flint-q8-benchmark)

Publication approved by Jaime. Original research documentation: CC BY 4.0; original publication scripts: MIT. Third-party terms and the evidence exclusions remain in [LICENSING.md](../LICENSING.md).

## Review material and assets

A versioned Release would provide a convenient fixed reference to the approved v5 package. Publication still requires Jaime's approval.

- [Public summary](../PUBLIC-SUMMARY.md) and [technical report](../TECHNICAL-REPORT.md).
- [Original summary PDF](../output/pdf/public-summary.pdf) and [original technical report PDF](../output/pdf/technical-report.pdf). Their November 5 status text/metadata is retained as part of the original package.
- Candidate asset: the original `phoenix-flint-q8-publication-v5.zip`, containing 363 canonical files, including all 308 supporting-evidence files. Its bytes match the canonical files at the pre-cleanup commit linked below. It has not been uploaded as a Release asset.
- Original ZIP SHA-256: `ddc0742cc55215dbc22fa25c49134bf1539c2316432ddbed7f343c06d707e779`.

The [pre-cleanup publication commit](https://github.com/drgf2y7cb7-afk/phoenix-flint-q8-benchmark/tree/fcb66fd2470cd934c2dd351db90fc46e58024173) records the original package plus the historical duplicate Batch folders. The original ZIP excludes those duplicates. Post-cleanup repository documentation and checksums differ from that original ZIP; the measurements and canonical evidence do not. If a Release is approved, identify the selected tag commit and label the original ZIP separately from GitHub-generated source archives.
