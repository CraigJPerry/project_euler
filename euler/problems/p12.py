# !/usr/bin/env python
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
from euler.helpers import first, flattened_product_combinations
from euler.problems.p3 import prime_factors as factorise


def triangle_numbers():
    """Infinite triangle numbers generator."""
    total = 0
    for i in itertools.count(start=1):
        total += i
        yield total


def all_divisors(number):
    """Determine all prime and composite factors of number."""
    prime_factors = tuple(factorise(number))
    composite_factors = flattened_product_combinations((1,) + prime_factors)
    return tuple(sorted(composite_factors))


class Problem12(unittest.TestCase):
    def test_triangle_numbers_generator_reproduces_example_numbers(self):
        self.assertTupleEqual((1, 3, 6, 10, 15, 21, 28, 36, 45, 55), tuple(first(10, triangle_numbers())))

    def test_factors_of_one(self):
        self.assertTupleEqual((1,), all_divisors(1))

    def test_table_of_given_factors(self):
        table = {
            1: (1,),
            3: (1, 3),
            6: (1, 2, 3, 6),
            10: (1, 2, 5, 10),
            15: (1, 3, 5, 15),
            21: (1, 3, 7, 21),
            28: (1, 2, 4, 7, 14, 28)
        }
        for triangle_num, factors in table.items():
            self.assertTupleEqual(factors, all_divisors(triangle_num))

    def test_count_of_divisors(self):
        self.assertGreater(len(all_divisors(28)), 5)


def main():
    for triangle_num in triangle_numbers():
        if len(all_divisors(triangle_num)) > 500:
            return triangle_num


if __name__ == "__main__":
    unittest.main()

