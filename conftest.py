"""Repo-root conftest: puts the repo root on sys.path so tests import as the
``tests.*`` namespace (same layout the suite had inside the tg_content_factory
monorepo before extraction)."""

import sys
from pathlib import Path

_ROOT = str(Path(__file__).resolve().parent)
if _ROOT not in sys.path:
    sys.path.insert(0, _ROOT)
