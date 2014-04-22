#!/usr/bin/env python
# encoding: utf-8


"""Helper functions for Project Euler."""

import itertools


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
    return [[int(cell) for cell in line.split() if cell] for line in grid.splitlines() if line and not line.isspace()]


def transpose(table):
    """Transpose a table (list of lists)."""
    return [list(sequence) for sequence in zip(*table)]  # zip returns tuples


def mirror(table):
    """Mirror a table around the vertical centrepoint."""
    return [list(reversed(row)) for row in table]


def product(sequence):
    """Compute the product of terms in a sequence."""
    return reduce(lambda x, y: int(x) * int(y), sequence)

