Project Euler
=============

My solutions for https://projecteuler.net/problems

* Friend key: 62329527622542_8f7a89d18ce714c27a29b4787041adcf
* Progress tracker: https://projecteuler.net/progress=CraigJPerry


About
-----

Written in Python so that i can practice with different styles &
technologies:

* Functional programming style (as opposed to object oriented)
* Cython for C native code extensions
* TODO: PyOpenCL for vectorised code on GPGPU / CPU vector instructions


Hacking
-------

I've created a small framework to simplify my workflow, which includes
building native extensions (automated).

To install:

    [user@host project_euler]$ mkvirtualenv -a $PWD -r requirements.txt project_euler
    (project_euler)[user@host project_euler]$ pip install --editable .

To run an individual solution:

    (project_euler)[user@host project_euler]$ euler p10  # Python implementation
    Problem p10: 142913828922 (1065.559 secs)
    (project_euler)[user@host project_euler]$ euler c10  # Cython implementation
    Problem c10: 142913828922 (0.261 secs)

To run all tests:

    (project_euler)[user@host project_euler]$ python -m unittest discover

To run only tests for problem 7:

    (project_euler)[user@host project_euler]$ python -m unittest euler.problems.p7  # Python impl
    (project_euler)[user@host project_euler]$ python -m unittest euler.problems.c7  # Cython impl
    OR
    (project_euler)[user@host project_euler]$ python euler/problems/p7.py

To recompile native-code extension modules after editing:

    (project_euler)[user@host project_euler]$ python setup.py build_ext --inplace

