#!/usr/bin/env python3
from __future__ import annotations
import sys
import unittest
from pathlib import Path

SRC = Path(__file__).resolve().parents[1] / 'src'
sys.path.insert(0, str(SRC))

from verinox_aegisloop import VerinoxEngine


class Spec1Smoke(unittest.TestCase):
    def test_construct_engine_from_code_folder(self):
        engine = VerinoxEngine()
        self.assertIsNotNone(engine)

    def test_loaded_from_code_folder_src(self):
        import verinox_aegisloop as pkg
        path = str(Path(pkg.__file__).resolve())
        self.assertIn('CODE FOLDER', path)
        self.assertIn('src', path)


if __name__ == '__main__':
    raise SystemExit(unittest.main(verbosity=2))
