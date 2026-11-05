# Draft GitHub release

**Title:** Flint Q8 on a mixed-generation dual-GPU workstation

**Author:** Jaime Lawson, Founder & Research Lead, Phoenix Applied Technologies.

This benchmark documents Flint Q8_0 (42.30 GB) through Colibri on Debian 13, a Ryzen 7 2700X, approximately 78 GiB RAM, RTX 4060 8 GB and GTX 1080 Ti 11 GB. Eight CPU inference workers and both GPUs contribute to the later whole-system results.

Completed explanatory responses measured 30.464 and 30.567 tokens/s on the same prompt and machine, with identical exported final text and reasoning. A harder coding repair measured 20.418 tokens/s and about 4:03 total; its saved fix passes 7/7 predefined tests. Rates include reasoning. The separate capped 31.194 tokens/s screen (31.2 rounded) remains preliminary and has not been independently repeated under the same protocol.

The report distinguishes decode rate, end-to-end latency and correctness. It retains the failed physics explanation, the baseline's two coding-test failures, incomplete attempts and reproduction limits. The small task set does not establish general accuracy or coding capability.

The repository contains a one-page summary, four-page technical report, unchanged sanitized evidence and verified offline test commands. Credit to Colibri's developers including Vincenzo Fornaro, Recursive and Unsloth. Codex/Sapphire assisted preparation and verification; these checks are not independent benchmark replication.

**Public benchmark contact:** [jmlawson@outlook.com](mailto:jmlawson@outlook.com)

[Repository (URL pending)](REPOSITORY_URL_PENDING)

Publication approved by Jaime. Original research documentation: CC BY 4.0; original publication scripts: MIT. Third-party terms and the evidence exclusions remain in LICENSING.md. Replace the repository URL placeholder during the authorized publication handoff.
