#!/usr/bin/env python
# encoding: utf-8


"""Summation of primes.

Project Euler, Problem 10. https://projecteuler.net/problem=10

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""

import unittest
from euler.helpers import below
from euler.problems.p7 import primes


# Problem 10 was solved with existing functionality, no new code.


class Problem10(unittest.TestCase):

    def test_validate_against_given_example(self):
        sum_below_ten = sum(below(10, primes()))
        self.assertEqual(17, sum_below_ten)


def main():
    return sum(below(2000000, primes()))


if __name__ == "__main__":
    unittest.main()

