#!/usr/bin/python
# -*- coding: utf-8 -*-
##########################################################################################
# author: Nikolas Schnellbaecher
# contact: khx0@posteo.net
# date: 2021-02-14
# file: math_core.py
# tested with python 3.7.6 and numpy 1.20.1
##########################################################################################

from math_core import number_of_digits

if __name__ == '__main__':

    # demo usage of the number_of_digits function

    my_list = [
        'item_01',
        'item_02',
        'item_03',
        'item_04',
        'item_05',
        'item_06',
        'item_07',
        'item_08',
        'item_09',
        'item_10',
    ]

    n_digits = number_of_digits(len(my_list))

    for i, item in enumerate(my_list):

        print("item #", str(i + 1).zfill(n_digits), "-->", item)

    print(f'{len(my_list)} items detected')
