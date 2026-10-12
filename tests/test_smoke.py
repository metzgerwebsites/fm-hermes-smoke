"""Smoke tests for the fm_hermes_smoke package.

Run them with `./run_tests.sh` or `python3 -m unittest discover -s tests -v`.
"""

import unittest

import fm_hermes_smoke


class SmokeMessageTest(unittest.TestCase):
    def test_smoke_message_returns_project_identifier(self):
        self.assertEqual(fm_hermes_smoke.smoke_message(), "fm-hermes-smoke")

    def test_package_exposes_version(self):
        self.assertEqual(fm_hermes_smoke.__version__, "0.1.0")


if __name__ == "__main__":
    unittest.main()