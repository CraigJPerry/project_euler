#!/usr/bin/env python
# encoding: utf-8


import math
import itertools


def multiples_of_3_and_5(until):
    return (x for x in xrange(1, until) if x % 3 == 0 or x % 5 == 0)


def fibonacci(a=1, b=2):
    """Infinite Fibonacci sequence generator."""
    while True:
        yield a
        a, b = b, b+a


def prime_factors(number):
    """Problem 3: Generate the prime factors of number."""
    while True:
        limit = int(math.sqrt(number) + 1)
        for i in xrange(2, limit):
            if number % i == 0:
                yield i
                number /= i
                break
        else:
            yield number
            break


def main():
    print "Problem 1: %d" % sum(multiples_of_3_and_5(1000))

    problem2 = itertools.takewhile(lambda x: x<4000000, fibonacci())
    print "Problem 2: %d" % sum(even for even in problem2 if even % 2 == 0)

    problem3 = prime_factors(600851475143)
    print "Problem 3: %d" % max(problem3)


if __name__ == "__main__":
    main()

