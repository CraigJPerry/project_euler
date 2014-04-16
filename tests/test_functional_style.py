#!/usr/bin/env python
# encoding: utf-8


import unittest
from euler.functional_style import (
    first, below, multiples_of_3_and_5, fibonacci, prime_factors,
    palindromes, smallest_evenly_divisible
)


class Problem1(unittest.TestCase):

    def setUp(self):
        self.answer = below(10, multiples_of_3_and_5())

    def test_given_sequence_for_natural_numbers_below_ten(self):
        self.assertTupleEqual(tuple(self.answer), (3, 5, 6, 9))

    def test_given_sum_for_natural_numbers_below_ten(self):
        self.assertEqual(sum(self.answer), 23)


class Problem2(unittest.TestCase):

    def test_given_example_first_ten_terms(self):
        terms = first(10, fibonacci())
        self.assertTupleEqual(tuple(terms), (1, 2, 3, 5, 8, 13, 21, 34, 55, 89))


class Problem3(unittest.TestCase):

    def verify_factors_for(self, number, expected_factors):
        """Given a number, verify expected prime factors are returned."""
        factors = prime_factors(number)
        self.assertTupleEqual(tuple(factors), expected_factors)

    def test_given_example_factors(self):
        self.verify_factors_for(13195, (5, 7, 13, 29))

    def test_simple_case_20(self):
        self.verify_factors_for(20, (2, 2, 5))

    def test_simple_case_21(self):
        self.verify_factors_for(21, (3, 7))


class Problem4(unittest.TestCase):

    def test_largest_two_digit_palindrome_example(self):
        largest = max(palindromes(2))
        self.assertEqual(largest[0], 9009)

    def test_largest_single_digit_palindrome(self):
        largest = max(palindromes(1))
        self.assertEqual(largest[0], 9)


class Problem5(unittest.TestCase):

    def test_given_example(self):
        self.assertEqual(smallest_evenly_divisible(1, 10), 2520)


if __name__ == "__main__":
    unittest.main()

