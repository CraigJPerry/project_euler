#!/usr/bin/env python
# encoding: utf-8


"""Smallest multiple.

Project Euler, Problem 5. https://projecteuler.net/problem=5

2520 is the smallest number that can be divided by each of the numbers
from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of
the numbers from 1 to 20?
"""

import unittest
import itertools


def smallest_evenly_divisible(start, end):
    """Find smallest number evenly divisible by all numbers
    between start and end.

    Start the search at 'end' and continue upwards since anything
    below 'end' will not be evenly divisible by 'end'. Take steps
    of size 'end' for the same reason.
    """
    all_nums = xrange(start, end + 1)

    for i in itertools.count(end, end):
        for j in all_nums:
            if i % j != 0:
                break
        else:
            return i


class Problem5(unittest.TestCase):

    def test_validate_against_given_example(self):
        self.assertEqual(2520, smallest_evenly_divisible(1, 10))


def main():
    return smallest_evenly_divisible(1, 20)


if __name__ == "__main__":
    unittest.main()

