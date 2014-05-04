#!/usr/bin/env python
# encoding: utf-8

"""Tests for individual problems are located in the solution module.

For example, in euler/problems/p11.py there is a TestCase instance. This
module is responsible adding all those test cases to the runner."""


import unittest
from os.path import join, dirname, pardir


def load_tests(loader, tests, pattern):
    problems_root_dir = join(dirname(__file__), pardir, "euler", "problems")
    pure_python_suite = loader.discover(problems_root_dir, pattern="*.py")
    return pure_python_suite


if __name__ == "__main__":
    unittest.main()

