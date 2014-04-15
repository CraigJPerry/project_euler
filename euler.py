#!/usr/bin/env python
# encoding: utf-8


def multiples_of_3_and_5(until):
    return (x for x in xrange(1, until) if x % 3 == 0 or x % 5 == 0)


def main():
    print "Problem 1: %d" % sum(multiples_of_3_and_5(1000))


if __name__ == "__main__":
    main()

