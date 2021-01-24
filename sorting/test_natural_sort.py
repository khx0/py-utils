#!/usr/bin/python
# -*- coding: utf-8 -*-
##########################################################################################
# author: Nikolas Schnellbaecher
# contact: khx0@posteo.net
# date: 2021-01-24
# file: test_natural_sort.py
# tested with python 3.7.6
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
Tested with pytest version 6.2.1.
'''

import platform
import unittest

from natural_sort import natural_sort
from natural_sort import natural_keys

class NaturalSortTest(unittest.TestCase):

    def test_01(self):
        """
        natrual sorting test case #1 using the natural_sort() function
        """

        # test input list
        test_list = ['file_111',
                     'file_99',
                     'file_10',
                     'file_1',
                     'file_100',
                     'file_9',
            ]

        # reference result for the specified test input
        ref_list = ['file_1',
                    'file_9',
                    'file_10',
                    'file_99',
                    'file_100',
                    'file_111'
            ]

        res = natural_sort(test_list)

        for i, item in enumerate(res):
            # print(i, item)
            self.assertTrue(item == ref_list[i])

        return None

    def test_02(self):
        """
        natrual sorting test case #2 using the list.sort(key=natural_keys()) syntax
        """

        # test input list
        a_list = ['file_111',
                  'file_99',
                  'file_10',
                  'file_1',
                  'file_100',
                  'file_9',
            ]

        # reference result for the specified test input
        ref_list = ['file_1',
                    'file_9',
                    'file_10',
                    'file_99',
                    'file_100',
                    'file_111'
            ]

        a_list.sort(key=natural_keys)

        for i, item in enumerate(a_list):
            # print(i, item)
            self.assertTrue(item == ref_list[i])

        return None

if __name__ == '__main__':

    print("/////////////////////////////////////////////////////////////////////////////")
    print("Running", __file__)
    print("/////////////////////////////////////////////////////////////////////////////")
    print("Python Interpreter Version =", platform.python_version())
    print("/////////////////////////////////////////////////////////////////////////////")
    print("Start testing ...")
    print("/////////////////////////////////////////////////////////////////////////////")

    unittest.main()
