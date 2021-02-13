#!/usr/bin/python
# -*- coding: utf-8 -*-
##########################################################################################
# author: Nikolas Schnellbaecher
# contact: khx0@posteo.net
# date: 2021-02-13
# file: test_matrixtools.py
# tested with python 3.7.6 and numpy 1.20.1
##########################################################################################

'''
--- Example invocations ---
Cd to the directory containing this script and there invoke
$python -m pytest (-v)
where python is your chosen python interpreter or alternatively only call
$pytest
or
$pytest -v
using the default python interpreter on your system.
The -v flag (equal to --verbose) sets the pytest mode to 'verbose'.
-------------------------------------------------------------------------------
To only run the tests in this test file use
$python -m pytest (-v) test_*.py
where test_*.py is the considered unit test script.
-------------------------------------------------------------------------------
plain unittest invocation
$python test_*.py
-------------------------------------------------------------------------------
Tested with pytest version 6.2.2.
'''

import platform
import unittest
import numpy as np

from math_core import number_of_digits

class MathCoreTest(unittest.TestCase):

    """
    # check if all edge cases are covered for the number_of_digits function
    """

    def test_01(self):

        n = 99
        n_digits = 2
        self.assertTrue(number_of_digits(n) == n_digits)

        n = 999
        n_digits = 3
        self.assertTrue(number_of_digits(n) == n_digits)

        n = 100
        n_digits = 3
        self.assertTrue(number_of_digits(n) == n_digits)

        n = 1
        n_digits = 1
        self.assertTrue(number_of_digits(n) == n_digits)

        n = 10
        n_digits = 2
        self.assertTrue(number_of_digits(n) == n_digits)

        n = 11
        n_digits = 2
        self.assertTrue(number_of_digits(n) == n_digits)

        n = 9
        n_digits = 1
        self.assertTrue(number_of_digits(n) == n_digits)

        return None

if __name__ == '__main__':

    unittest.main()
