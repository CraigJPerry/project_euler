# !/usr/bin/env python
# encoding: utf-8


"""Longest Collatz sequence.

Project Euler, Problem 14. https://projecteuler.net/problem=14

The following iterative sequence is defined for the set of positive
integers:

    n → n/2 (n is even)
    n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following
sequence:

    13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

It can be seen that this sequence (starting at 13 and finishing at 1)
contains 10 terms. Although it has not been proved yet (Collatz Problem),
it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""

import unittest


def collatz(n):
    """Terms of the collatz sequence starting at n."""
    while n != 1:
        yield n
        if n % 2:
            n = (3 * n) + 1
        else:
            n /= 2
    yield 1


class Problem14(unittest.TestCase):

    def test_given_sequence(self):
        self.assertEqual((13, 40, 20, 10, 5, 16, 8, 4, 2, 1), tuple(collatz(13)))


def main():
    return max(
        (len(tuple(collatz(i))), i) for i in range(1, 1000001)
    )


if __name__ == "__main__":
    unittest.main()

