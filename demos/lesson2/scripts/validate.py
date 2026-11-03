#!/usr/bin/env python3
"""Deterministic structural checks for a safely isolated demo vault."""
from pathlib import Path
root=Path(__file__).resolve().parents[1]
required=['general/INDEX.md','general/MEMORY.md','general/agent/BOOTSTRAP.md','general/agent/SESSION_CLOSE.md','areas/Research/transit-employment/transit-employment_INDEX.md','areas/Research/transit-employment/transit-employment_CURRENT_STATE.md']
missing=[x for x in required if not (root/x).exists()]
if missing:
 print('FAIL — missing:',missing);raise SystemExit(1)
import subprocess,sys
result=subprocess.run([sys.executable,str(root/'scripts/audit.py')])
if result.returncode:raise SystemExit(1)
print('OK — canonical structure and demo maintenance checks passed')
