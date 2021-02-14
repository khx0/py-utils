#!/usr/bin/python
# -*- coding: utf-8 -*-
##########################################################################################
# author: Nikolas Schnellbaecher
# contact: khx0@posteo.net
# date: 2021-02-14
# file: math_core.py
# tested with python 3.7.6 and numpy 1.20.1
##########################################################################################

import numpy as np

def number_of_digits(n: int) -> int:
    '''
    Returns the number of digits of a given integer n.
    '''
    if np.isclose(n, 0.0):
        return 1
    else:
        return int(np.floor(np.log10(np.abs(n)) + 1))

if __name__ == '__main__':

    pass
