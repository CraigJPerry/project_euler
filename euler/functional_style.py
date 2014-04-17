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


# Problem 10 was solved with existing functionality, no new code.


def horizontal_sequencer(n, table):
    """Problem 11: Chunkify a table into horizontal sequences of n."""
    return (row[offset:offset + n] for row in table for offset in xrange(len(row) - n + 1))


def vertical_sequencer(n, table):
    """Problem 11: Chunkify a table into vertical sequences of n. Same
    problem as horizontal_sequencer but with the table transposed"""
    return horizontal_sequencer(n, transpose(table))


def grid_sequencer(n=4, grid=None):
    """Problem 11: break a grid into sequences of n from the vertical,
    horizontal, left diagonal and right diagonal directions."""
    if grid is None:
        grid = """
            08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08
            49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00
            81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65
            52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91
            22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80
            24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50
            32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70
            67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21
            24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72
            21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95
            78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92
            16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57
            86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58
            19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40
            04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66
            88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69
            04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36
            20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16
            20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54
            01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48
        """
    table = tablify(grid)
    return itertools.chain(
        horizontal_sequencer(n, table),
        vertical_sequencer(n, table)
    )


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


def tablify(grid):
    """Parse a textual table into a list of lists."""
    return [[int(cell) for cell in line.split() if cell] for line in grid.splitlines() if not line.isspace()]


def transpose(table):
    """Transpose a table."""
    return zip(*table)


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

