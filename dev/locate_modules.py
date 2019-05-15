#!/usr/bin/python
# -*- coding: utf-8 -*-
##########################################################################################
# author: Nikolas Schnellbaecher
# contact: khx0@posteo.net
# date: 2019-05-15
# file: locate_modules.py
##########################################################################################

'''
To locate a python module, call its *.__file__ property.
This applies to all modules that you import in a given python file,
i.e. both to packaged modules and to user written local python modules
This can be very useful if you have many complicated include 
path structures and multiple versions of a given module with identical 
names. Then using *.__file__ will tell you the path of the module 
which is actually included. This can also help to decipher
include path precedence. This is illustrated below for the 
three standard modules numpy, scipy and matplotlib.
'''

import sys
import os
import datetime

import numpy as np
import scipy
import matplotlib as mpl

now = datetime.datetime.now()
now = "{}-{}-{}".format(now.year, str(now.month).zfill(2), str(now.day).zfill(2))

BASEDIR = os.path.dirname(os.path.abspath(__file__))
RAWDIR = os.path.join(BASEDIR, 'raw')
OUTDIR = os.path.join(BASEDIR, 'out')

if __name__ == '__main__':

    print(__name__)

    # useful meta properties of any python script
    print(__file__)
    print(os.path.abspath(__file__))
    print(os.path.dirname(os.path.abspath(__file__)))

    print("np.__version__ =", np.__version__)
    print("np.__file__ =", np.__file__)

    print("scipy.__version__ =", scipy.__version__)
    print("scipy.__file__ =", scipy.__file__)

    print("mpl.__version__ =", mpl.__version__)
    print("mpl.__file__ =", mpl.__file__)
