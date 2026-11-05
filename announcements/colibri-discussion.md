# Draft Colibri GitHub Discussion

**Title:** Flint Q8 measurements on RTX 4060 + GTX 1080 Ti, with reproducible evidence

**Jaime Lawson - Founder & Research Lead, Phoenix Applied Technologies**

This report follows Flint Q8_0 (42.30 GB) from a single RTX 4060 through earlier 4060 + GTX 1070 experiments to a 4060 + GTX 1080 Ti configuration in Colibri v2.1.0. The workstation uses Debian 13, a Ryzen 7 2700X and approximately 78 GiB RAM.

With eight CPU inference workers, dense computation on the 4060 and experts on both GPUs plus CPU/RAM, completed explanatory controls measured 30.464 and 30.567 tokens/s. Both use the same prompt and identical exported outputs, so they are not independent replications. The complete coding repair measured 20.418 tokens/s, about 4:03 end to end, with 7/7 saved checks passing. All rates include reasoning.

A separate 768-token screen reached 31.194 tokens/s. That truncated result remains preliminary. The report keeps short CUDA/Vulkan comparisons separate from complete-answer performance and records cache, CPU-thread, memory and expert-history details. Changes in hardware, output length and cache state prevent a universal backend ranking.

The physics accuracy failure and failed baseline tests remain visible. Broader accuracy, cold-cache performance and independent repetition are open work. The one-page summary, four-page report and full supporting evidence are available at the repository below, including commands verified against the packaged directory structure.

Thanks to Colibri's developers, including Vincenzo Fornaro, and to Recursive and Unsloth. Codex/Sapphire assisted evidence preparation and test replay; this is not independent replication or a claim of developer endorsement.

**Public benchmark contact:** [jmlawson@outlook.com](mailto:jmlawson@outlook.com)

[Repository (URL pending)](REPOSITORY_URL_PENDING)

Publication approved by Jaime. Original research documentation: CC BY 4.0; original publication scripts: MIT. Preserve the third-party notices and historical-evidence qualifications in LICENSING.md; replace the repository URL placeholder before posting.
