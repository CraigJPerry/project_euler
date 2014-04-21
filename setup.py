#!/usr/bin/env python
# encoding: utf-8


"""My attempts at Project Euler in various coding styles."""


from setuptools import setup, find_packages
from distutils.extension import Extension
from Cython.Distutils import build_ext


__version__ = "0.1.2"
README = open("README.rst").read()
REQUIREMENTS = open("requirements.txt").readlines()


setup(
    name="euler",
    version=__version__,
    description=__doc__,
    long_description=README,
    author="Craig J Perry",
    author_email="craigp84@gmail.com",
    install_requires=REQUIREMENTS,
    packages=find_packages(exclude=["tests"]),
    cmdclass = {'build_ext': build_ext},
    ext_modules = [Extension("euler.problems.seven", ["euler/problems/seven.pyx"])],
    entry_points={
        "console_scripts": [
            "euler = euler.runner:main",
        ]
    }
)

