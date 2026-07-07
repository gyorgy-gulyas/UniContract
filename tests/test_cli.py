import unittest
import subprocess
import sys
import os
import tempfile
import argparse

import unicontract.__main__ as cli_main

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def run_cli(*args):
    return subprocess.run(
        [sys.executable, "-m", "unicontract", *args],
        capture_output=True, text=True, cwd=ROOT)


class TestCli(unittest.TestCase):
    """UNI-17: the CLI was untested (argparse + end-to-end)."""

    def test_abort_flags_are_proper_booleans(self):
        # UNI-06: the flags used to default to the truthy strings "True"/"False"
        # combined with store_true, so both were always truthy.
        add_args = getattr(cli_main, "__add_known_arguments")
        parser = argparse.ArgumentParser()
        add_args(parser)

        args = parser.parse_args(["-i", "x.contract"])
        self.assertIs(args.abort_on_error, True)     # default enabled
        self.assertIs(args.abort_on_warning, False)  # default disabled

        args = parser.parse_args(["-i", "x", "--no-abort-on-error", "--abort-on-warning"])
        self.assertIs(args.abort_on_error, False)
        self.assertIs(args.abort_on_warning, True)

    def test_missing_input_reports_the_filename(self):
        # UNI-09: used to print the builtin `input` object instead of the path.
        r = run_cli("-i", "no_such_file_xyz.contract", "-e", "json")
        self.assertNotEqual(r.returncode, 0)
        self.assertIn("no_such_file_xyz.contract", r.stdout + r.stderr)

    def test_help_lists_emitters_without_rust(self):
        r = run_cli("-h")
        self.assertEqual(r.returncode, 0)
        self.assertNotIn("rust", (r.stdout + r.stderr).lower())

    def test_json_emit_end_to_end(self):
        with tempfile.TemporaryDirectory() as d:
            src = os.path.join(d, "x.contract")
            with open(src, "w") as f:
                f.write("namespace N {\n    interface I {\n    }\n}\n")
            r = run_cli("-i", src, "-e", "json", "-o", d)
            self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
            self.assertTrue(any(f.endswith(".json") for f in os.listdir(d)),
                            f"no .json emitted: {os.listdir(d)}")


if __name__ == "__main__":
    unittest.main()
