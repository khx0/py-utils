#!/usr/bin/python
# -*- coding: utf-8 -*-
##########################################################################################
# author: Nikolas Schnellbaecher
# contact: khx0@posteo.net
# date: 2021-02-13
# file: math_core.py
# tested with python 3.7.6 and numpy 1.20.1
##########################################################################################

import numpy as np

def number_of_digits(n: int) -> int:
    '''
    Returns the number of digits of a given integer n.
    '''
    return int(np.floor(np.log10(np.abs(n)) + 1))

if __name__ == '__main__':

    pass

    '''
    # check if all edge cases are covered
    # convert into unit test and demonstration example
    print(number_of_digits(99))
    print(number_of_digits(999))
    print(number_of_digits(100))
    print(number_of_digits(1))
    print(number_of_digits(10))
    print(number_of_digits(11))
    print(number_of_digits(9))

    # print fonts which are available for the given matplotlib installation
    flist = mpl.font_manager.get_fontconfig_fonts()

    n_digits = number_of_digits(len(flist))

    for i, fname in enumerate(flist):

        print("font #", str(i + 1).zfill(n_digits), "-->", fname)

    print(f'{len(flist)} fonts detected')
    '''
