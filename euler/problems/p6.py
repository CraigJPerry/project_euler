#!/usr/bin/env python
# encoding: utf-8


"""Sum square difference.

Project Euler, Problem 6. https://projecteuler.net/problem=6

The sum of the squares of the first ten natural numbers is,
    12 + 22 + ... + 102 = 385

The square of the sum of the first ten natural numbers is,
    (1 + 2 + ... + 10)2 = 552 = 3025

Hence the difference between the sum of the squares of the first ten
natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one
hundred natural numbers and the square of the sum.
"""

import unittest


def sum_square_difference(upper_limit):
    """Find the difference of sum of squares and square of
    sum for natural numbers to upper_limit."""
    naturals = range(upper_limit + 1)
    sum_of_squares = reduce(lambda x, y: x + y*y, naturals)
    square_of_sum = sum(naturals) ** 2
    return square_of_sum - sum_of_squares


class Problem6(unittest.TestCase):

    def test_validate_against_given_example(self):
        self.assertEqual(2640, sum_square_difference(10))


def main():
    return sum_square_difference(100)


if __name__ == "__main__":
    unittest.main()

