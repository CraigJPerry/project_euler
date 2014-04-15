#!/usr/bin/env python
# encoding: utf-8


import unittest
import itertools
from euler import multiples_of_3_and_5, fibonacci, prime_factors


class Problem1(unittest.TestCase):

    def test_given_example_natural_numbers_below_ten(self):
        answer = tuple(multiples_of_3_and_5(10))
        self.assertTupleEqual(answer, (3, 5, 6, 9))
        self.assertEqual(sum(answer), 23)


class Problem2(unittest.TestCase):

    def test_given_example_first_ten_terms(self):
        terms = tuple(itertools.islice(fibonacci(), 10))
        self.assertTupleEqual(terms, (1, 2, 3, 5, 8, 13, 21, 34, 55, 89))


class Problem3(unittest.TestCase):

    def test_given_example_factors(self):
        factors = tuple(prime_factors(13195))
        self.assertTupleEqual(factors, (5, 7, 13, 29))


if __name__ == "__main__":
    unittest.main()

