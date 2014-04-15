#!/usr/bin/env python
# encoding: utf-8


import itertools


def multiples_of_3_and_5(until):
    return (x for x in xrange(1, until) if x % 3 == 0 or x % 5 == 0)


def fibonacci(a=1, b=2):
    """Infinite Fibonacci sequence generator."""
    while True:
        yield a
        a, b = b, b+a


def main():
    print "Problem 1: %d" % sum(multiples_of_3_and_5(1000))

    problem2 = itertools.takewhile(lambda x: x<4000000, fibonacci())
    print "Problem 2: %d" % sum(even for even in problem2 if even % 2 == 0)


if __name__ == "__main__":
    main()

