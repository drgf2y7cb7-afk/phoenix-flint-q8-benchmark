#!/usr/bin/env python3
"""Replay the archived coding fixtures. No model, server, network or external package needed.

Run from repository root: python3 tools/verify_coding.py
The original fixture bytes are copied to a disposable directory. Each child has
CPU/address-space/file-size limits and a timeout. Expected baseline failures are
reported as failures, and are required for an overall successful verification.
"""
from pathlib import Path
import json
import os
import re
import resource
import shutil
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[1]
FIXTURES = ROOT / 'supporting-evidence/tests/async-cache'
FILES = ['test_cache.py', 'buggy_cache.py', 'flint_fixed_cache.py', 'q8_fixed_cache.py']

def limits():
    resource.setrlimit(resource.RLIMIT_CPU, (10, 10))
    resource.setrlimit(resource.RLIMIT_AS, (512 * 1024 * 1024, 512 * 1024 * 1024))
    resource.setrlimit(resource.RLIMIT_FSIZE, (1024 * 1024, 1024 * 1024))
    resource.setrlimit(resource.RLIMIT_CORE, (0, 0))

def main():
    missing = [name for name in FILES if not (FIXTURES / name).is_file()]
    if missing:
        print('Missing archived fixture files: ' + ', '.join(missing), file=sys.stderr)
        return 2
    results = []
    with tempfile.TemporaryDirectory(prefix='flint-coding-check-') as td:
        work = Path(td)
        for name in FILES:
            shutil.copyfile(FIXTURES / name, work / name)
            (work / name).chmod(0o444)
        env = {'PATH': os.environ.get('PATH', ''), 'PYTHONDONTWRITEBYTECODE': '1', 'LC_ALL': 'C.UTF-8'}
        for module, expected_status, expected_failures in [
            ('buggy_cache', 1, 2), ('flint_fixed_cache', 0, 0), ('q8_fixed_cache', 0, 0)
        ]:
            command = [sys.executable, '-B', 'test_cache.py', module]
            run = subprocess.run(command, cwd=work, env=env, text=True,
                                 capture_output=True, timeout=20, preexec_fn=limits)
            output = run.stdout + run.stderr
            print(f'--- {module}: exit {run.returncode} ---')
            print(output.rstrip())
            passed = len(re.findall(r'^test_.* \.\.\. ok$', output, re.MULTILINE))
            failed = len(re.findall(r'^test_.* \.\.\. FAIL$', output, re.MULTILINE))
            expected = (run.returncode == expected_status and passed == 7 - expected_failures
                        and failed == expected_failures and 'Ran 7 tests' in output)
            results.append({'module': module, 'exit_status': run.returncode,
                            'passed': passed, 'failed': failed,
                            'expected_result_reproduced': expected})
    print(json.dumps(results, indent=2))
    if not all(item['expected_result_reproduced'] for item in results):
        print('FAIL: archived test outcomes were not reproduced.', file=sys.stderr)
        return 1
    print('PASS: expected baseline failures and both 7/7 patched results reproduced. No inference executed.')
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
