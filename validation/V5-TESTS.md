# Verification record

The final published commands were executed verbatim in a clean copy of the repository. No model inference was performed. The scripts use Python 3.13.5 on Linux with the standard library only.

The archived direct commands work when run from their specified fixture directory. The new repository-root runner makes that path explicit and handles the baseline's expected nonzero exit without hiding it. Original test cases and both model patches are unchanged.

| Command | Working directory | Exit | Result |
|---|---|---:|---|
| `python3 tools/verify_coding.py` | `.` | 0 | [Expected results reproduced](v5-01-root-coding-runner.txt) |
| `python3 supporting-evidence/scripts/rebuild_tables.py --check` | `.` | 0 | [Evidence/table checks passed](v5-02-root-evidence-check.txt) |
| `PYTHONDONTWRITEBYTECODE=1 python3 test_cache.py buggy_cache` | `supporting-evidence/tests/async-cache` | 1 | [5 passed, 2 failed](v5-03-buggy-baseline.txt) |
| `PYTHONDONTWRITEBYTECODE=1 python3 test_cache.py flint_fixed_cache` | `supporting-evidence/tests/async-cache` | 0 | [7 passed, 0 failed](v5-04-single-gpu-fix.txt) |
| `PYTHONDONTWRITEBYTECODE=1 python3 test_cache.py q8_fixed_cache` | `supporting-evidence/tests/async-cache` | 0 | [7 passed, 0 failed](v5-05-dual-gpu-fix.txt) |
| `python3 scripts/rebuild_tables.py --check` | `supporting-evidence` | 0 | [Evidence/table checks passed](v5-06-archived-root-check.txt) |
| `python3 scripts/rebuild_tables.py` | `supporting-evidence` | 0 | [Evidence/table checks passed](v5-07-archived-rebuild.txt) |

**The buggy baseline intentionally fails two tests.** It is not a passing implementation. Each saved patched implementation passes all seven. The root runner returns zero only when all these expected outcomes are observed. These are fixture replays, not new model generations.

The preserved evidence checker verifies 40 run/case rows with 401 checks in `--check` mode (398 when regenerating tables). Rebuilding in the disposable copy does not modify the archived evidence delivered in this package.

CPU, memory, output-size and timeout limits were applied. The root runner also uses a disposable directory containing only the reviewed fixtures. The commands require Linux/POSIX; no cross-platform runner claim is made.

See [v5-test-commands.json](v5-test-commands.json) for exact commands, working directories, statuses and the full execution record. [Integrity and redaction checks](v5-audit.json) cover the final publication artifacts and preserved evidence.
