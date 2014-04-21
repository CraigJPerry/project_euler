"""10001st prime (Cython implementation).

Project Euler, Problem 7. https://projecteuler.net/problem=7

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can
see that the 6th prime is 13.

What is the 10 001st prime number?
"""

import unittest
from libc.math cimport log, sqrt
from types import BuiltinFunctionType
from cpython.mem cimport PyMem_Malloc, PyMem_Free


cdef int how_high(int nth):
    """Use the prime counting function to estimate how high to count in
    search for a given number of primes."""
    cdef int i = 1, estimate = 1
    while estimate < nth:
        i += 1
        estimate = 2 ** i / <int>log(2 ** i)
    return 2 ** i


def primes(int limit):
    """Faster (Cython generated native code) prime numbers sieve. Cython
    does not yet support implementing generators."""
    cdef:
        int i, j
        int *is_prime = <int *>PyMem_Malloc(limit * sizeof(int))
    try:
        if not is_prime:
            raise MemoryError()

        # Assume everything's prime to begin with
        for i in range(limit):
            is_prime[i] = 1
        is_prime[0] = 0  # 1 is not a prime (zero indexed array)

        # Sieve the primes...
        for i in range(2, <long>sqrt(limit) + 1):
            if is_prime[i-1]:
                # ...and flag the composites (NB: squared optimisation)
                for j in range(i*i, limit+1, i):
                    is_prime[j-1] = 0

        return [i+1 for i in range(limit) if is_prime[i]]
    finally:
        PyMem_Free(is_prime)


class Problem7InCython(unittest.TestCase):

    def test_can_load_native_code_func(self):
        self.assertIsInstance(primes, BuiltinFunctionType)

    def test_numerical_accuracy_of_first_ten_primes(self):
        expected = [2, 3, 5, 7]
        self.assertListEqual(expected, primes(10))


def main():
    n = 10001
    prime_count_estimate = how_high(n)
    return primes(prime_count_estimate)[n-1]


if __name__ == "__main__":
    unittest.main()

