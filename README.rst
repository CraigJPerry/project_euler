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
    (project_euler)[user@host project_euler]$
