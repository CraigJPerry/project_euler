#!/usr/bin/env python
# encoding: utf-8


"""Craig's Project Euler solutions implemented as Python generators
in a (largely) functional style of programming."""

import math
import itertools


def multiples_of_3_and_5():
    """Problem 1: Unbounded generator yielding multiples of 3 or 5."""
    return (x for x in itertools.count(1) if x % 3 == 0 or x % 5 == 0)


def fibonacci(a=1, b=2):
    """Problem 2: Infinite Fibonacci sequence generator."""
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


def largest_palindrome(places):
    """Problem 4: Largest palindrome from 2 factors up to 'places' wide."""
    maximum_value = int(math.pow(10, places) - 1)
    for i in xrange(maximum_value, 0, -1):
        for j in xrange(maximum_value, 0, -1):
            palindrome = str(i * j)
            if palindrome == palindrome[::-1]:
                return int(palindrome)


################################################################################
# Helper Functions
################################################################################


def below(n, generator):
    """Yield generator while value is below n."""
    return itertools.takewhile(lambda x: x < n, generator)


def first(n, generator):
    """Yield first n items from generator."""
    return itertools.islice(generator, n)


def main():
    problem1 = below(1000, multiples_of_3_and_5())
    print "Problem 1: %d" % sum(problem1)

    problem2 = below(4000000, fibonacci())
    print "Problem 2: %d" % sum(even for even in problem2 if even % 2 == 0)

    problem3 = prime_factors(600851475143)
    print "Problem 3: %d" % max(problem3)

    problem4 = largest_palindrome(3)
    print "Problem 4: %d" % problem4


if __name__ == "__main__":
    main()

