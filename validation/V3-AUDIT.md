> Historical record: describes its named prior revision. Current licenses and publication authorization are in [V5-AUDIT.md](V5-AUDIT.md).

# Historical V3 verification

This record describes the prior v3 review. The current contact update is documented in [V4-AUDIT.md](V4-AUDIT.md).

This attribution and publication revision changes no benchmark measurements, original evidence, fixture logic or verification runner. The 308 supporting-evidence files and all prior-version files were checked byte-for-byte. The technical report's scientific body matches v2 exactly after removing the added credit paragraph; the summary results table is identical.

The prior clean-copy seven-command record and logs are retained in [VERIFICATION.md](VERIFICATION.md). All published coding commands remain identical. Both root entry points were also run once in a new clean V3 repository copy on Linux/Python 3.13.5:

| Command from repository root | Exit | Result |
|---|---:|---|
| `python3 tools/verify_coding.py` | 0 | [Baseline 5 pass/2 fail; both saved patches 7 pass/0 fail](v3-coding-runner.txt) |
| `python3 supporting-evidence/scripts/rebuild_tables.py --check` | 0 | [40 rows, 401 checks](v3-evidence-check.txt) |

The baseline failure is required and remains visible. These are saved-fixture replays, not inference runs. No new accuracy or performance measurements were produced.

Both PDFs were rendered and all five pages visually inspected. The public summary is one page; the technical report is four pages. Author metadata is `Jaime Lawson, Founder & Research Lead, Phoenix Applied Technologies`; the document text and credits identify the same author and assistance.

The Colibri LICENSE, NOTICE and THIRD_PARTY_NOTICES match both the saved checkout and its recorded pinned Git revision. The font-family notice is included. See the [file inventory](third-party-inventory.csv) and [rights decisions](../LICENSING.md). License selection and generated-output/local-fixture provenance clearance remain pending.

The final scan checks text, extracted PDF text and metadata for private paths, credentials, network identifiers and unapproved email addresses. The approved author name and public upstream attribution are retained. Markdown local targets are checked; `REPOSITORY_URL_PENDING` is an intentional unresolved placeholder in four announcement/brief files. At the v3 review, the public contact had not yet been approved. The current approved contact is recorded in [CONTACT.md](../governance/CONTACT.md); the repository URL remains pending.

The archive excludes local Git metadata, private provenance and working files. Only the approved name and `user.useConfigOnly` are configured in the local repository. Email/account verification remains pending; there are no commits or remotes and no global identity changes.

The v2 validation records inside this candidate describe their original validation event, not a new independent replication. [V3 machine-readable audit](v3-audit.json) records this revision. Private original evidence and prior packages remain preserved; no production configuration or public destination was changed.
