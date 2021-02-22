#!/usr/bin/python
# -*- coding: utf-8 -*-
##########################################################################################
# author: Nikolas Schnellbaecher
# contact: khx0@posteo.net
# date: 2021-02-22
# file: assertions.py
# tested with python 3.7.6
##########################################################################################

import numpy as np

'''
To check if a variable is a floating point variable, one can use the tuple
(np.floating, float) in the isinstance call, as illustrated below.
This checks for multiple different float types.
'''

if __name__ == '__main__':

    x = 2.0 # built in float
    print(x, '--> of type', type(x))
    assert isinstance(x, (np.floating, float)), "Float assertion failed."

    x = np.float64(2.0)
    print(x, '--> of type', type(x))
    assert isinstance(x, (np.floating, float)), "Float assertion failed."

    x = np.float32(2.0)
    print(x, '--> of type', type(x))
    assert isinstance(x, (np.floating, float)), "Float assertion failed."
