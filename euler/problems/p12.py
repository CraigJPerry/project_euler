#!/usr/bin/env python
# encoding: utf-8


"""Highly divisible triangular number.

Project Euler, Problem 12. https://projecteuler.net/problem=12

The sequence of triangle numbers is generated by adding the
natural numbers. So the 7th triangle number would be
1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:

    1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

Let us list the factors of the first seven triangle numbers:

     1: 1
     3: 1,3
     6: 1,2,3,6
    10: 1,2,5,10
    15: 1,3,5,15
    21: 1,3,7,21
    28: 1,2,4,7,14,28

We can see that 28 is the first triangle number to have over five divisors.

What is the value of the first triangle number to have over five hundred
divisors?
"""

import unittest
import itertools
from euler.helpers import first


def triangle_numbers():
    total = 0
    for i in itertools.count(start=1):
        total += i
        yield total


class Problem12(unittest.TestCase):

    def test_triangle_numbers_generator_correctly_reproduces_given_example_numbers(self):
        self.assertTupleEqual((1, 3, 6, 10, 15, 21, 28, 36, 45, 55), tuple(first(10, triangle_numbers())))


def main():
    raise NotImplementedError


if __name__ == "__main__":
    unittest.main()

