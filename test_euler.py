#!/usr/bin/env python
# encoding: utf-8


import unittest
from euler import multiples_of_3_and_5


class Problem1(unittest.TestCase):

    def test_given_example_natural_numbers_below_ten(self):
        answer = list(multiples_of_3_and_5(10))
        self.assertListEqual(answer, [3, 5, 6, 9])
        self.assertEqual(sum(answer), 23)

    def test_required_answer_for_multiples_below_one_thousand(self):
        answer = sum(multiples_of_3_and_5(1000))
        self.assertEqual(answer, 233168)


if __name__ == "__main__":
    unittest.main()

