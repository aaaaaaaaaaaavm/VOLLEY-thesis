"""Compatibility entry point for the current academic check."""
from pathlib import Path
import runpy
runpy.run_path(str(Path(__file__).with_name("check_acr1.py")),run_name="__main__")
