#!/usr/bin/env python
# encoding: utf-8


"""Project Euler, Problem 1.

https://projecteuler.net/problem=1

If we list all the natural numbers below 10 that are multiples of 3 or
5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""

import unittest
import itertools
from euler.helpers import below


def multiples_of_3_and_5():
    """Unbounded generator yielding multiples of 3 or 5."""
    return (x for x in itertools.count(1) if x % 3 == 0 or x % 5 == 0)


class Problem1(unittest.TestCase):

    def setUp(self):
        self.answer = below(10, multiples_of_3_and_5())

    def test_given_sequence_for_natural_numbers_below_ten(self):
        self.assertTupleEqual((3, 5, 6, 9), tuple(self.answer))

    def test_given_sum_for_natural_numbers_below_ten(self):
        self.assertEqual(23, sum(self.answer))


def main():
    return sum(below(1000, multiples_of_3_and_5()))


if __name__ == "__main__":
    unittest.main()

