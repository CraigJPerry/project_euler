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


def palindromes(places):
    """Problem 4: Generate all palindromes of 2 factors  up to 'places' wide."""
    maximum_value = int(math.pow(10, places))
    for i in xrange(maximum_value):
        for j in xrange(maximum_value):
            candidate = str(i * j)
            if candidate == candidate[::-1]:
                palindrome = int(candidate)
                yield palindrome, i, j


def smallest_evenly_divisible(start, end):
    """Problem 5: Find smallest number evenly divisible by all numbers
    between start and end."""
    all_nums = range(start, end + 1)

    # Start the search at 'end' and continue upwards, since anything
    # below 'end' will not be evenly divisible by 'end'. Take steps
    # of size 'end' for the same reason.
    for i in itertools.count(end, end):
        for j in all_nums:
            if i % j != 0:
                break
        else:
            return i


def sum_square_difference(upper_limit):
    """Problem 6: Find the difference of sum of squares and square of
    sum for natural numbers to upper_limit."""
    naturals = range(upper_limit + 1)
    sum_of_squares = reduce(lambda x, y: x + y*y, naturals)
    square_of_sum = sum(naturals) ** 2
    return square_of_sum - sum_of_squares


def primes():
    """Problem 7: Infinite prime numbers generator."""
    seen = set()
    for candidate in itertools.count(2):
        for prime in seen:
            if candidate % prime == 0:
                break
        else:
            seen.add(candidate)
            yield candidate


def products_of(n=5, sequence=None):
    """Problem 8: Products of n consecutive digits in sequence."""
    if sequence is None:
        sequence = """\
            73167176531330624919225119674426574742355349194934
            96983520312774506326239578318016984801869478851843
            85861560789112949495459501737958331952853208805511
            12540698747158523863050715693290963295227443043557
            66896648950445244523161731856403098711121722383113
            62229893423380308135336276614282806444486645238749
            30358907296290491560440772390713810515859307960866
            70172427121883998797908792274921901699720888093776
            65727333001053367881220235421809751254540594752243
            52584907711670556013604839586446706324415722155397
            53697817977846174064955149290862569321978468622482
            83972241375657056057490261407972968652414535100474
            82166370484403199890008895243450658541227588666881
            16427171479924442928230863465674813919123162824586
            17866458359124566529476545682848912883142607690042
            24219022671055626321111109370544217506941658960408
            07198403850962455444362981230987879927244284909188
            84580156166097919133875499200524063689912560717606
            05886116467109405077541002256983155200055935729725
            71636269561882670428252483600823257530420752963450
        """
    sequence = str(sequence).replace(" ", "").replace("\n", "")
    sliding_window = (sequence[offset:offset+n] for offset in xrange(len(sequence) - n + 1))
    for chunk in sliding_window:
        yield reduce(lambda x, y: int(x)*int(y), chunk)


def is_pythagorean_triplet(a, b, c):
    """Problem 9: Identify pythagorean triplets."""
    return a < b < c and a ** 2 + b ** 2 == c ** 2


def pythagorean_triplet_finder(sums_to):
    """Problem 9: Return triplet which sums to given value."""
    for c in xrange(sums_to-2, 0, -1):
        for b in xrange(c-1, 0, -1):
            for a in xrange(b-1, 0, -1):
                if is_pythagorean_triplet(a, b, c) and sum((a, b, c)) == sums_to:
                    return (a, b, c)


def product_of_ptriplet_which(sums_to=1000):
    """Problem 9: Find the product of the pythagorean triplet which sums to n."""
    triplet = pythagorean_triplet_finder(sums_to)
    if triplet:
        return reduce(lambda x, y: x*y, triplet), triplet
    return None, None


################################################################################
# Helper Functions
################################################################################


def below(n, generator):
    """Yield generator while value is below n."""
    return itertools.takewhile(lambda x: x < n, generator)


def first(n, generator):
    """Yield first n items from generator."""
    return itertools.islice(generator, n)


def even(generator):
    """Yield only the even terms from generator."""
    return (i for i in generator if i % 2 == 0)


def nth(n, generator):
    """Return nth item from generator."""
    return next(itertools.islice(generator, n-1, n))


def main():
    problem1 = below(1000, multiples_of_3_and_5())
    print "Problem 1: %d" % sum(problem1)

    problem2 = even(below(4000000, fibonacci()))
    print "Problem 2: %d" % sum(problem2)

    problem3 = prime_factors(600851475143)
    print "Problem 3: %d" % max(problem3)

    problem4 = max(palindromes(3))
    print "Problem 4: %d (%d * %d)" % problem4

    problem5 = smallest_evenly_divisible(1, 20)
    print "Problem 5: %d" % problem5

    problem6 = sum_square_difference(100)
    print "Problem 6: %d" % problem6

    problem7 = nth(10001, primes())
    print "Problem 7: %d" % problem7

    problem8 = products_of()
    print "Problem 8: %d" % max(problem8)

    problem9 = product_of_ptriplet_which()
    a, b, c = problem9[1]
    print "Problem 9: %s (%d < %d < %d)" % (problem9[0], a, b, c)

    problem10 = sum(below(2000000, primes()))
    print "Problem 10: %d" % problem10


if __name__ == "__main__":
    main()

