#!/usr/bin/env python
# encoding: utf-8


"""Project Euler, Problem 3.

https://projecteuler.net/problem=3

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

import math
import unittest


def prime_factors(number):
    """Generate the prime factors of number."""
    while True:
        limit = int(math.sqrt(number) + 1)
        for i in xrange(2, limit):
            if number % i == 0:
                yield i
                number /= i
                break
        else:
            yield number
            break


class Problem3(unittest.TestCase):

    def verify_factors_for(self, number, expected_factors):
        """Given a number, verify expected prime factors are returned."""
        factors = prime_factors(number)
        self.assertTupleEqual(expected_factors, tuple(factors))

    def test_validate_against_given_example(self):
        self.verify_factors_for(13195, (5, 7, 13, 29))

    def test_for_positive_result(self):
        self.verify_factors_for(20, (2, 2, 5))

    def test_for_negative_result(self):
        self.verify_factors_for(21, (3, 7))


def main():
    return max(prime_factors(600851475143))


if __name__ == "__main__":
    unittest.main()

