# Publication status and cleanup checklist

Updated November 6, 2026. The approved v5 benchmark is [publicly available on GitHub](https://github.com/drgf2y7cb7-afk/phoenix-flint-q8-benchmark). The [Colibri announcement](https://github.com/JustVugg/colibri/discussions/208#discussioncomment-19445667) is already published.

## Completed

- Jaime approved public release and selected CC BY 4.0 for original research documentation and MIT for the two original benchmark scripts. The exact scope, third-party terms and historical/generated-output qualifications in [LICENSING.md](LICENSING.md) are unchanged.
- Public identity/contact remains Jaime Lawson, Founder & Research Lead, Phoenix Applied Technologies; [jmlawson@outlook.com](mailto:jmlawson@outlook.com). That contact is not authorized as a Git commit email.
- README and public-summary status reflect publication. The four announcement/reference files link to the actual repository. The Colibri text is archival; Reddit and Hacker News plans are canceled, not pending.
- The 212 files in `Batch 2 of 4` (98), `Batch 3 of 4` (81) and `Batch 4 of 4` (33) were matched by SHA-256 to canonical paths and by Git blob identity to the approved package before removing the redundant folders. No unique files were found. Git history retains the removed copies.
- All 308 canonical supporting-evidence files remain byte-identical to the approved v5 package. Original technical reports, PDFs, scripts, attribution and license notices are unchanged. PDF status text/metadata and historical audits remain dated snapshots, not current publication instructions.
- Seven existing offline verification commands reproduced their expected results: the buggy baseline fails two tests, both saved fixes pass 7/7, evidence checking passes 401 checks over 40 rows, and table regeneration passes 398 checks. No inference was run.
- `licenses/LICENSE-SCOPE.csv` retains exactly the same paths, license treatments and limitations; only affected file hashes were refreshed. `SHA256SUMS` reflects the current canonical tree. The approved original ZIP remains unchanged.

## Optional Release, awaiting owner approval

No GitHub Release or tag was created. A `v5.0` Release could give readers a convenient versioned reference. [Release notes and candidate-asset details](announcements/github-release.md) are prepared for review using the existing approved materials. Publishing a Release still requires explicit approval. No new announcement is planned.

## Boundaries retained

Preserve original measurements, preliminary-result qualifications, physics-failure disclosures and provenance limitations. Do not rerun inference or change production systems or local model files for publication housekeeping. Preserve the archived evidence and prior versions. [Current audit](validation/V5-AUDIT.md) | [Git attribution and privacy](governance/GIT-IDENTITY.md).
