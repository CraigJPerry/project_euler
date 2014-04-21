#!/usr/bin/env python
# encoding: utf-8


import unittest
from euler.runner import main
from cStringIO import StringIO


class CanInvokeProblemRunner(unittest.TestCase):

    def setUp(self):
        self.output = StringIO()

    def test_can_run_individual_problems_by_number(self):
        main(["euler", "p1"], self.output)
        self.assertIn("Problem 1:", self.output.getvalue())

    def test_invalid_problem_number_reports_appropriate_error_message(self):
        main(["euler", "invalid"], self.output)
        self.assertIn("ERROR:", self.output.getvalue())

    def test_missing_problem_number_gives_usage_message(self):
        main(["euler"], self.output)
        self.assertIn("usage:", self.output.getvalue())

    def test_output_includes_runtime(self):
        main(["euler", "p1"], self.output)
        self.assertRegexpMatches(self.output.getvalue(), "\(\d+\.\d{3} secs\)")


if __name__ == "__main__":
    unittest.main()

