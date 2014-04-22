#!/usr/bin/env python
# encoding: utf-8


"""Special Pythagorean triplet.

Project Euler, Problem 9. https://projecteuler.net/problem=9

A Pythagorean triplet is a set of three natural numbers, a < b < c, for
which,
    a2 + b2 = c2

For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

import unittest
from euler.helpers import product


def is_pythagorean_triplet(a, b, c):
    """Problem 9: Identify pythagorean triplets."""
    return a < b < c and a ** 2 + b ** 2 == c ** 2


def pythagorean_triplet_finder(sums_to):
    """Problem 9: Return triplet which sums to given value."""
    for c in xrange(sums_to-2, 0, -1):
        for b in xrange(c-1, 0, -1):
            for a in xrange(b-1, 0, -1):
                if is_pythagorean_triplet(a, b, c) and sum((a, b, c)) == sums_to:
                    return a, b, c


def product_of_ptriplet_which(sums_to=1000):
    """Problem 9: Find the product of the pythagorean triplet which sums to n."""
    triplet = pythagorean_triplet_finder(sums_to)
    if triplet:
        return product(triplet), triplet
    return None, None


class Problem9(unittest.TestCase):

    def test_validate_against_given_example(self):
        self.assertTrue(is_pythagorean_triplet(3, 4, 5))

    def test_for_negative_result(self):
        self.assertFalse(is_pythagorean_triplet(3, 4, 6))

    def test_triplet_finder_should_return_a_tuple_when_found(self):
        sequence = pythagorean_triplet_finder(12)
        self.assertTupleEqual((3, 4, 5), sequence)

    def test_triplet_finder_should_return_none_when_not_found(self):
        sequence = pythagorean_triplet_finder(13)
        self.assertIsNone(sequence)

    def test_product_of_ptriplet_should_return_a_two_tuple_of_product_and_the_responsible_triplet(self):
        product, triplet = product_of_ptriplet_which(sums_to=12)
        self.assertEqual(60, product)
        self.assertTupleEqual(triplet, (3, 4, 5))


def main():
    calculated_product, triplet = product_of_ptriplet_which()
    a, b, c = triplet
    return "%s (%d < %d < %d)" % (calculated_product, a, b, c)


if __name__ == "__main__":
    unittest.main()

