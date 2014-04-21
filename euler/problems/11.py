#!/usr/bin/env python
# encoding: utf-8


"""Largest product in a grid.

Project Euler, Problem 11. https://projecteuler.net/problem=11

In the 20×20 grid below, four numbers along a diagonal line have been
marked in red.

08 02 22 97 38 15 00 40  00  75  04  05  07 78 52 12 50 77 91 08
49 49 99 40 17 81 18 57  60  87  17  40  98 43 69 48 04 56 62 00
81 49 31 73 55 79 14 29  93  71  40  67  53 88 30 03 49 13 36 65
52 70 95 23 04 60 11 42  69  24  68  56  01 32 56 71 37 02 36 91
22 31 16 71 51 67 63 89  41  92  36  54  22 40 40 28 66 33 13 80
24 47 32 60 99 03 45 02  44  75  33  53  78 36 84 20 35 17 12 50
32 98 81 28 64 23 67 10 *26* 38  40  67  59 54 70 66 18 38 64 70
67 26 20 68 02 62 12 20  95 *63* 94  39  63 08 40 91 66 49 94 21
24 55 58 05 66 73 99 26  97  17 *78* 78  96 83 14 88 34 89 63 72
21 36 23 09 75 00 76 44  20  45  35 *14* 00 61 33 97 34 31 33 95
78 17 53 28 22 75 31 67  15  94  03  80  04 62 16 14 09 53 56 92
16 39 05 42 96 35 31 47  55  58  88  24  00 17 54 24 36 29 85 57
86 56 00 48 35 71 89 07  05  44  44  37  44 60 21 58 51 54 17 58
19 80 81 68 05 94 47 69  28  73  92  13  86 52 17 77 04 89 55 40
04 52 08 83 97 35 99 16  07  97  57  32  16 26 26 79 33 27 98 66
88 36 68 87 57 62 20 72  03  46  33  67  46 55 12 32 63 93 53 69
04 42 16 73 38 25 39 11  24  94  72  18  08 46 29 32 40 62 76 36
20 69 36 41 72 30 23 88  34  62  99  69  82 67 59 85 74 04 36 16
20 73 35 29 78 31 90 01  74  31  49  71  48 86 81 16 23 57 05 54
01 70 54 71 83 51 54 69  16  92  33  48  61 43 52 01 89 19 67 48

The product of these numbers is 26 × 63 × 78 × 14 = 1788696.

What is the greatest product of four adjacent numbers in the same
direction (up, down, left, right, or diagonally) in the 20×20 grid?
"""

import unittest
import itertools
from euler.helpers import tablify, product, mirror, transpose


def horizontal_sequencer(n, table):
    """Chunkify a table into horizontal sequences of n."""
    return (row[offset:offset + n] for row in table for offset in xrange(len(row) - n + 1))


def vertical_sequencer(n, table):
    """Chunkify a table into vertical sequences of n. Same
    problem as horizontal_sequencer but with the table transposed"""
    return horizontal_sequencer(n, transpose(table))


def left_diagonal_sequencer(n, table):
    """Chunkify a table into left-diagonal sequences of n."""
    x_limit = len(table[0]) - n + 1
    y_limit = len(table) - n + 1
    return ([table[i][j] for (i, j) in zip(xrange(x, x+n), xrange(y, y+n))] for x in xrange(x_limit) for y in xrange(y_limit))


def right_diagonal_sequencer(n, table):
    """Chunkify a table into right-diagonal sequences of n.
    Same problem as LDS but with the table mirrored on a vertical axis."""
    return left_diagonal_sequencer(n, mirror(table))


def grid_sequencer(n=4, grid=None):
    """Break a grid into sequences of n from the vertical,
    horizontal, left diagonal and right diagonal directions."""
    if grid is None:
        grid = """
            08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08
            49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00
            81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65
            52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91
            22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80
            24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50
            32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70
            67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21
            24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72
            21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95
            78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92
            16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57
            86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58
            19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40
            04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66
            88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69
            04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36
            20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16
            20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54
            01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48
        """
    table = tablify(grid)
    return itertools.chain(
        horizontal_sequencer(n, table),
        vertical_sequencer(n, table),
        left_diagonal_sequencer(n, table),
        right_diagonal_sequencer(n, table)
    )


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


def main():
    return max(product(sequence) for sequence in grid_sequencer())


if __name__ == "__main__":
    unittest.main()

