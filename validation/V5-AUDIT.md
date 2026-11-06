# V5 release audit

## Publication cleanup update (November 6, 2026)

The approved v5 package is [published](https://github.com/drgf2y7cb7-afk/phoenix-flint-q8-benchmark), and the [Colibri announcement](https://github.com/JustVugg/colibri/discussions/208#discussioncomment-19445667) is live. This update supersedes the publication-pending wording in the historical packaging audit below. Reddit and Hacker News plans are canceled. No new GitHub Release, tag or announcement was published.

Before cleanup, all 363 canonical files matched the approved original ZIP and the live Git tree at `fcb66fd2470cd934c2dd351db90fc46e58024173`. All 212 files in the three Batch folders were exact redundant copies: 98 in Batch 2, 81 in Batch 3 and 33 in Batch 4. SHA-256 values matched their canonical files, and both paths referenced the same Git blobs. No unique evidence or documentation was present. Only those redundant folders were removed.

All 308 canonical evidence files, both original PDFs, the technical report, verification scripts, attribution and license notices remain unchanged. All seven offline commands reproduced their expected outcomes: baseline 5 pass / 2 fail, both fixes 7/7, evidence check 401 checks / 40 rows, regeneration 398 checks. These are replay checks, not independent replication or new inference.

Current README/summary and announcement links are corrected. The file-by-file license scope retains the same paths and treatments; only hashes for edited documentation were refreshed. Root SHA-256 checksums were refreshed accordingly. The original v5 ZIP hash remains `ddc0742cc55215dbc22fa25c49134bf1539c2316432ddbed7f343c06d707e779`. Original PDFs retain their historical status text/metadata and remain one and four pages.

[Release checklist](../RELEASE-CHECKLIST.md) records the current state. [Draft v5.0 release notes](../announcements/github-release.md) identify the existing reports and verified candidate ZIP for owner review. The machine-readable audit below is the historical November 5 packaging record, not a report of current publication status.

## Historical packaging audit (November 5, 2026)

Jaime approved public release of the verified v4 package and selected CC BY 4.0 for original research documentation and MIT for original benchmark scripts. This fresh v5 copy applies only those scoped licensing and publication-status changes. It preserves the approved public identity and contact. Nothing was published to GitHub from this executor.

## Evidence, results and tests

All 308 supporting-evidence files are byte-identical to v4, including original logs, raw samples, configurations, expert-history seeds, test cases and saved model output. Every prior-package file captured before the revision was also hash-checked unchanged. The scientific report body and summary/README results sections are unchanged; only license/status text and current verification links changed.

All seven documented offline commands were run verbatim from their stated working directories in one clean copy, with limits and timeouts. [V5-TESTS.md](V5-TESTS.md) records outputs and exit codes. The baseline still fails two tests (5 pass / 2 fail); both saved fixes pass 7/7. The evidence checker passed 401 checks across 40 run/case rows; table regeneration passed its 398 checks. Twelve published command occurrences match the commands executed. No new model inference or performance benchmark was run.

The completed explanatory rates remain 30.464 and 30.567 tokens/s on the same machine/prompt with matching exported outputs, not independent replications. Coding remains 20.418 tokens/s and 242.71-243.50 seconds end to end. The separate 31.194 tokens/s capped run remains preliminary. Reasoning, decode/prompt/end-to-end boundaries, physics failure, initial truncation, dependent tests and all benchmark limitations remain visible.

## Licensing and publication readiness

The complete CC BY 4.0 and MIT texts are included. [LICENSE-SCOPE.csv](../licenses/LICENSE-SCOPE.csv) identifies exact paths and hashes. MIT is limited to `tools/verify_coding.py` and `supporting-evidence/scripts/rebuild_tables.py`. The archived fixtures, Flint-generated code/transcripts and Colibri patch are not blanket-relicensed. The Colibri and font license/notices remain byte-identical to v4. No model weights or runtime binaries are included.

No concrete license conflict was identified in the inspected artifacts. Specific provenance questions remain: authorship/license of the fixture and harness reused from the earlier 176B experiment, and generated-output rights/source provenance for the saved Flint transcripts/fixes. They are explicitly excluded from the new grants, without claiming exclusive ownership. The unresolved base-model revision is a provenance limitation; there are no shipped weights needing a new grant. These are qualifications, not a claim of established infringement. [LICENSING.md](../LICENSING.md) records the exact scope and questions.

The package passes the scoped technical, test, integrity and privacy checks for the publication handoff. It is not an unconditional legal clearance of every historical/generated artifact. Publication authorization and the license choice are already complete; no repeat approval is requested here. The parent still needs the actual repository destination/URL and an authorized publication route. Repository-local Git email remains unset; use only a verified account-specific noreply address, not the public contact.

## Final artifact checks

PDFs are one and four pages. All five pages were visually inspected after rendering; author metadata and public contact are correct. Text and PDF metadata were scanned for private paths, credentials, network identifiers and unapproved emails; only the expressly approved contact is permitted. Local links are checked, with exactly four intentional `REPOSITORY_URL_PENDING` targets in announcements/briefs. No live URL is invented. The root manifest and extracted ZIP are hash-verified.

No Git settings, production configurations or original evidence were changed; no repository was created, no GitHub upload/post was attempted, and no new authentication or permissions were requested. Private review delivery of the ZIP is separate from public publication. Earlier audits remain marked historical. [Machine-readable V5 audit](v5-audit.json).
