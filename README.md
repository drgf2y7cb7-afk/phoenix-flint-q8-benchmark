# Flint Q8 Benchmark

**Jaime Lawson** | Founder & Research Lead, **Phoenix Applied Technologies**

Local AI inference, hardware optimization, offline AI infrastructure and practical model evaluation.

**Release package v5 - November 5, 2026. Public release approved; not yet published.**

## System and model

Debian 13; AMD Ryzen 7 2700X; approximately 78 GiB RAM; RTX 4060 8 GB + GTX 1080 Ti 11 GB. Flint Q8_0: **42.30 GB**; Colibri v2.1.0. Later CUDA tests used eight inference CPU workers, dense computation on the 4060, and expert caches on both GPUs. These are whole-system results, including CPU/RAM, not standalone GPU scores.

## Results at a glance

All rates include reasoning. Completed rates use final token counts / decode-loop time; sampled rates are the last active cumulative average.

| Test | Decode rate | End-to-end time | Evidence status |
|---|---:|---:|---|
| Full explanatory response, control A | 30.464 tok/s | 61.15-61.94 s | Completed; 1,819 tokens |
| Full explanatory response, control B | **30.567 tok/s** | 60.14-60.94 s | Completed; same 1,819-token output |
| Full coding repair | **20.418 tok/s** | **242.71-243.50 s** | Completed; fix passed 7/7 tests |
| 768-token explanatory screen | **31.194 tok/s** | 25.24-26.03 s | **Preliminary** sampled rate; truncated |

The two explanatory controls verified similar performance on the same machine and prompt, with identical exported final text and reasoning. They are not independent replications. **31.2 tok/s remains preliminary:** one capped run, no same-protocol independent repeat, and an unresolved early UI-temperature caveat. Sources: [E1-E4 in the technical report](TECHNICAL-REPORT.md#evidence-key).

## Optimization and correctness

Automatic CUDA cache allocation measured 31.194 versus 27.830 tok/s with a fixed allowance in the short screen, a **12.1% observed increase**, subject to the same preliminary caveat. On later full responses, prompt-aware cache replanning was **14.3% slower**, and moving dense computation to the Ti was **11.0% slower**. These are workload-specific observations; faster decode did not always mean a shorter answer.

The async-cache repair passed seven predefined checks in both saved completed attempts. The first single-GPU attempt had truncated before a final answer. The baseline code fails two tests. **The physics failure remains documented:** several insulation responses misrepresented GPU thermal-interface materials as barriers that improve cooling by slowing heat toward the cooler. The explanatory timing test was not an accuracy pass. No general coding or accuracy score is claimed.

## Read, verify, review

[Four-page technical report](output/pdf/technical-report.pdf) | [One-page summary](output/pdf/public-summary.pdf) | [Technical Markdown](TECHNICAL-REPORT.md) | [Separate supporting evidence](supporting-evidence/README.md)

From the repository root, with Python 3.8+ on Linux (verified with 3.13.5):

```bash
python3 tools/verify_coding.py
python3 supporting-evidence/scripts/rebuild_tables.py --check
```

The first command requires the baseline's two failures and both patched 7/7 results. Neither command runs inference. [Current test verification](validation/V5-TESTS.md). Original evidence and the prior package are preserved; Jaime has approved public release.

## Repository contents and attribution

| Path | Purpose |
|---|---|
| `PUBLIC-SUMMARY.md`, `output/pdf/public-summary.pdf` | One-page public overview |
| `TECHNICAL-REPORT.md`, `output/pdf/technical-report.pdf` | Four-page methodology, results and limitations |
| `supporting-evidence/` | Unchanged 308-file sanitized evidence package, including original detailed reports |
| `tools/`, `validation/` | Offline coding runner, saved command outputs and release audit |
| `announcements/` | GitHub/Colibri drafts; factual Reddit/HN briefs for the author |
| `licenses/`, `THIRD-PARTY-NOTICES.md` | Applicable upstream notices and scope |
| `governance/`, `RELEASE-CHECKLIST.md` | Contact, Git identity and approval decisions |

Credit to Colibri's developers, including Vincenzo Fornaro, Recursive for Flint, and Unsloth for the GGUF distribution. OpenAI Codex and Sapphire assisted evidence organization, calculations, test replay and drafting. Jaime Lawson is the named author and research lead; he has approved public release. These assistance checks are not independent benchmark replication. [Full credits](CREDITS.md).

**Licenses selected by Jaime:** CC BY 4.0 for the original research documentation and MIT for the original benchmark scripts explicitly listed in the license scope. Third-party material keeps its existing terms; raw evidence and model-generated code are not blanket-relicensed. [Licensing and rights scope](LICENSING.md) | [Third-party inventory](THIRD-PARTY-NOTICES.md).

**Public benchmark contact:** [jmlawson@outlook.com](mailto:jmlawson@outlook.com). Jaime expressly approved this address for public benchmark inquiries. [Contact scope](governance/CONTACT.md). Announcement links use the explicit `REPOSITORY_URL_PENDING` placeholder until the repository exists and its URL is approved. [Release checklist](RELEASE-CHECKLIST.md) | [Current release audit](validation/V5-AUDIT.md).

The material inside `supporting-evidence/` is an immutable prior review snapshot. Its historical publication text is retained as evidence; use this root README and `announcements/` for the current release. The historical records retain earlier review status; [LICENSING.md](LICENSING.md) records the licenses now selected.
