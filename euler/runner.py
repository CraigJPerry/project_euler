#!/usr/bin/env python
# encoding: utf-8


"""Application launcher."""

import sys
import time
import importlib


def import_problem_module(problem_number):
    """Retrieve module for the given problem."""
    return importlib.import_module("euler.problems.%s" % problem_number)


def render(problem_number, result, destination, runtime):
    """Output formatted result for given problem to destination."""
    print >> destination, "Problem %s: %s (%.3f)" % (problem_number, result, runtime)


def usage(destination):
    """Help."""
    print >> destination, "usage: euler <problem number>"
    return 1


def error(destination, message):
    """Report a problem."""
    print >> destination, "ERROR: %s" % message
    return 2


def run(module):
    """Run a module and capture runtime statistics."""
    start = time.time()
    result = module.main()
    end = time.time()
    return result, end - start


def main(argv=None, output=None):
    """Application entry point."""

    if argv is None:
        argv = sys.argv
    if output is None:
        output = sys.stdout

    if len(argv) != 2:
        return usage(output)

    problem_number = argv[1]

    try:
        module = import_problem_module(problem_number)
    except ImportError:
        return error(output, "No such problem: %s" % problem_number)

    result, runtime = run(module)

    render(problem_number, result, output, runtime)


if __name__ == "__main__":
    sys.exit(main())

