#!/usr/bin/env python
# encoding: utf-8


"""Project Euler, Problem 4.

https://projecteuler.net/problem=4

A palindromic number reads the same both ways. The largest palindrome
made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

import unittest


def palindromes(places):
    """Generate all palindromes of 2 factors  up to 'places' wide."""
    maximum_value = 10 ** places
    for i in xrange(maximum_value):
        for j in xrange(maximum_value):
            candidate = str(i * j)
            if candidate == candidate[::-1]:
                palindrome = int(candidate)
                yield palindrome, i, j


class Problem4(unittest.TestCase):

    def test_validate_against_given_example(self):
        largest = max(palindromes(2))
        self.assertEqual(9009, largest[0])

    def test_edge_case_of_single_digit(self):
        largest = max(palindromes(1))
        self.assertEqual(9, largest[0])


def main():
    largest = max(palindromes(3))
    return "%d (%d * %d)" % largest


if __name__ == "__main__":
    unittest.main()

