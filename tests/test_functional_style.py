#!/usr/bin/env python
# encoding: utf-8


import unittest
from euler.functional_style import *


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


class Problem6(unittest.TestCase):

    def test_given_example(self):
        self.assertEqual(sum_square_difference(10), 2640)


class Problem7(unittest.TestCase):

    def test_given_example(self):
        self.assertEqual(nth(6, primes()), 13)


class Problem8(unittest.TestCase):

    def test_simple_example(self):
        products = products_of(2, "12345")
        self.assertEqual(max(products), 4*5)

    def test_harder_example(self):
        products = products_of(3, "1234567890")
        self.assertEqual(max(products), 7*8*9)


class Problem9(unittest.TestCase):

    def test_valid_ptriplet(self):
        self.assertTrue(is_pythagorean_triplet(3, 4, 5))

    def test_non_ptriplet(self):
        self.assertFalse(is_pythagorean_triplet(3, 4, 6))

    def test_triplet_finder_returns_tuple_when_found(self):
        sequence = pythagorean_triplet_finder(12)
        self.assertTupleEqual(sequence, (3, 4, 5))

    def test_triplet_finder_returns_none_when_not_found(self):
        sequence = pythagorean_triplet_finder(13)
        self.assertIsNone(sequence)

    def test_product_of_ptriplet(self):
        product, triplet = product_of_ptriplet_which(sums_to=12)
        self.assertEqual(product, 60)
        self.assertTupleEqual((3, 4, 5), triplet)


class Problem10(unittest.TestCase):

    def test_simple_case(self):
        sum_below_ten = sum(below(10, primes()))
        self.assertEqual(sum_below_ten, 17)


class Problem11(unittest.TestCase):

    TEST_TABLE = tablify("""\
        08 02 22 97 38
        49 49 99 40 17
        81 49 31 73 55
        52 70 95 23 04
        22 31 16 71 51
    """)

    def test_horizontal_sequencer(self):
        sequence = horizontal_sequencer(3, self.TEST_TABLE)
        self.assertEqual(next(sequence), [8, 2, 22])
        self.assertEqual(next(sequence), [2, 22, 97])

    def test_vertical_sequencer(self):
        sequence = vertical_sequencer(3, self.TEST_TABLE)
        self.assertEqual(next(sequence), [8, 49, 81])
        self.assertEqual(next(sequence), [49, 81, 52])


if __name__ == "__main__":
    unittest.main()

