#!/usr/bin/env python
# encoding: utf-8


import unittest
from types import BuiltinFunctionType
from euler.native_primes import primes


class CompilationWorked(unittest.TestCase):

    def test_can_load_native_code_func(self):
        self.assertIsInstance(primes, BuiltinFunctionType)


class NumericalAccuracy(unittest.TestCase):

    def test_first_ten_primes(self):
        #           1      2     3     4      5     6      7     8      9      10
        expected = [False, True, True, False, True, False, True, False, False, False]
        self.assertListEqual(expected, primes(10))


if __name__ == "__main__":
    unittest.main()

