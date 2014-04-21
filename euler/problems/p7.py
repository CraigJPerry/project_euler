"""10001st prime (pure Python implementation).

Project Euler, Problem 7. https://projecteuler.net/problem=7

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can
see that the 6th prime is 13.

What is the 10 001st prime number?
"""

import unittest
import itertools
from euler.helpers import nth


def primes():
    """Infinite prime numbers generator (pure Python implementation)."""
    seen = set()
    for candidate in itertools.count(2):
        for prime in seen:
            if candidate % prime == 0:
                break
        else:
            seen.add(candidate)
            yield candidate


class Problem7InPurePython(unittest.TestCase):

    def test_validate_against_given_example(self):
        self.assertEqual(13, nth(6, primes()))


def main():
    return nth(10001, primes())


if __name__ == "__main__":
    unittest.main()

