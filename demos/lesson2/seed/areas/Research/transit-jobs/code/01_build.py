#!/usr/bin/env python3
"""Confirm the synthetic panel path. Does not download anything."""
from pathlib import Path
p = Path(__file__).resolve().parents[1] / "data" / "synthetic_panel.csv"
print("SIMULATED panel:", p.name, "bytes", p.stat().st_size)
