"""Faster (Cython generated native code) prime numbers generator."""

from cpython.mem cimport PyMem_Malloc, PyMem_Free
from libc.math cimport sqrt


def primes(int limit):
    """Problem 7: List all prime numbers up to limit. Cython does
       not yet support generators."""
    cdef:
        int i, j
        int *is_prime = <int *>PyMem_Malloc(limit * sizeof(int))
    try:
        if not is_prime:
            raise MemoryError()

        # Assume everything's prime to begin with
        for i in range(limit):
            is_prime[i] = 1

        # Sieve the primes...
        for i in range(2, <long>sqrt(limit)):
            if is_prime[i]:
                # ...and flag the composites (NB: squared optimisation)
                for j in range((i*i)-1, limit, i):
                    is_prime[j] = 0

        return [bool(is_prime[i]) for i in range(limit)]
    finally:
        PyMem_Free(is_prime)

