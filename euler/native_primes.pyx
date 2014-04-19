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

