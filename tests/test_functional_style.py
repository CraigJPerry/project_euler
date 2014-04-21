#!/usr/bin/env python
# encoding: utf-8


import unittest
from euler.functional_style import *


class Problem1(unittest.TestCase):

    def setUp(self):
        self.answer = below(10, multiples_of_3_and_5())

    def test_given_sequence_for_natural_numbers_below_ten(self):
        self.assertTupleEqual((3, 5, 6, 9), tuple(self.answer))

    def test_given_sum_for_natural_numbers_below_ten(self):
        self.assertEqual(23, sum(self.answer))


class Problem2(unittest.TestCase):

    def test_validate_against_given_example(self):
        terms = first(10, fibonacci())
        self.assertTupleEqual((1, 2, 3, 5, 8, 13, 21, 34, 55, 89), tuple(terms))


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


class Problem4(unittest.TestCase):

    def test_validate_against_given_example(self):
        largest = max(palindromes(2))
        self.assertEqual(9009, largest[0])

    def test_edge_case_of_single_digit(self):
        largest = max(palindromes(1))
        self.assertEqual(9, largest[0])


class Problem5(unittest.TestCase):

    def test_validate_against_given_example(self):
        self.assertEqual(2520, smallest_evenly_divisible(1, 10))


class Problem6(unittest.TestCase):

    def test_validate_against_given_example(self):
        self.assertEqual(2640, sum_square_difference(10))


class Problem7(unittest.TestCase):

    def test_validate_against_given_example(self):
        self.assertEqual(13, nth(6, pyprimes()))


class Problem8(unittest.TestCase):

    def test_group_by_two(self):
        products = products_of(2, "12345")
        self.assertEqual(4*5, max(products))

    def test_highest_somewhere_in_the_middle(self):
        products = products_of(3, "1234567890")
        self.assertEqual(7*8*9, max(products))


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


class Problem10(unittest.TestCase):

    def test_validate_against_given_example(self):
        sum_below_ten = sum(below(10, pyprimes()))
        self.assertEqual(17, sum_below_ten)


class Problem11(unittest.TestCase):

    TEST_TABLE = tablify("""
        08 02 22 97 38
        49 49 99 40 17
        81 49 31 73 55
        52 70 95 23 04
        22 31 16 71 51
    """)

    def test_horizontal_sequencer_in_regular_circumstances(self):
        sequence = horizontal_sequencer(3, self.TEST_TABLE)
        self.assertEqual([8, 2, 22], next(sequence))
        self.assertEqual([2, 22, 97], next(sequence))

    def test_horiztonal_sequencer_in_single_chunks(self):
        sequence = horizontal_sequencer(1, self.TEST_TABLE)
        self.assertEqual([8], next(sequence))
        self.assertEqual([2], next(sequence))

    def test_horiztonal_sequencer_in_row_sized_chunks(self):
        sequence = horizontal_sequencer(5, self.TEST_TABLE)
        self.assertEqual([8, 2, 22, 97, 38], next(sequence))
        self.assertEqual([49, 49, 99, 40, 17], next(sequence))

    def test_horiztonal_sequencer_in_oversized_sized_chunks(self):
        sequence = horizontal_sequencer(6, self.TEST_TABLE)
        self.assertRaises(StopIteration, next, sequence)

    def test_vertical_sequencer_in_regular_circumstances(self):
        sequence = vertical_sequencer(3, self.TEST_TABLE)
        self.assertEqual([8, 49, 81], next(sequence))
        self.assertEqual([49, 81, 52], next(sequence))

    def test_left_diagonal_sequencer_in_regular_circumstances(self):
        sequence = left_diagonal_sequencer(3, self.TEST_TABLE)
        self.assertEqual([8, 49, 31], next(sequence))
        self.assertEqual([2, 99, 73], next(sequence))

    def test_left_diagonal_sequencer_wrapping_around_at_end_of_row(self):
        sequence = left_diagonal_sequencer(4, self.TEST_TABLE)
        self.assertEqual([8, 49, 31, 23], next(sequence))
        self.assertEqual([2, 99, 73, 4], next(sequence))
        self.assertEqual([49, 49, 95, 71], next(sequence))

    def test_right_diagonal_sequencer_wrapping_around_at_end_of_row(self):
        sequence = right_diagonal_sequencer(4, self.TEST_TABLE)
        self.assertEqual([38, 40, 31, 70], next(sequence))

    def test_grid_sequencer_end_to_end(self):
        small_table = """
           08 02 22
           49 49 99
           81 49 31
        """
        sequence = grid_sequencer(3, small_table)

        # Horizontal sequencer
        self.assertEqual([8, 2, 22], next(sequence))
        self.assertEqual([49, 49, 99], next(sequence))
        self.assertEqual([81, 49, 31], next(sequence))

        # Vertical sequencer
        self.assertEqual([8, 49, 81], next(sequence))
        self.assertEqual([2, 49, 49], next(sequence))
        self.assertEqual([22, 99, 31], next(sequence))

        # Left diagonal sequencer
        self.assertEqual([8, 49, 31], next(sequence))

        # Right diagonal sequencer
        self.assertEqual([22, 49, 81], next(sequence))

        self.assertRaises(StopIteration, next, sequence)


if __name__ == "__main__":
    unittest.main()

