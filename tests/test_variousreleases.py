#!/usr/bin/env python3
"""Verification tests for variousreleases PDF and HTML artifacts."""

import os
import unittest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class TestVariousReleases(unittest.TestCase):
    def test_release_artifacts_exist(self):
        for rel in (
            "README.md",
            "output.pdf",
            "output_white.pdf",
            "output.html",
            "output_white.html",
            "FABLE.pdf",
            "CV_EN.pdf",
            "CV_DE.pdf",
            "CV_RU.pdf",
            "antivibecoding.odp",
        ):
            path = os.path.join(ROOT, rel)
            self.assertTrue(os.path.isfile(path), f"Missing {path}")
            self.assertGreater(os.path.getsize(path), 0)


if __name__ == "__main__":
    unittest.main()
