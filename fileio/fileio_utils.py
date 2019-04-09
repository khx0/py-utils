#!/usr/bin/python
# -*- coding: utf-8 -*-
##########################################################################################
# author: Nikolas Schnellbaecher
# contact: khx0@posteo.net
# date: 2019-04-09
# file: fileio_utils.py
##########################################################################################

import sys
import os
import datetime

def ensure_dir(dir):
    if not os.path.exists(dir):
        os.makedirs(dir)

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

    # print system path
    print(sys.path)

    ensure_dir(RAWDIR)
    ensure_dir(OUTDIR)

    dirname_with_timestamp = "data_" + now
    ensure_dir(dirname_with_timestamp)

    '''
    Using python >3.5 os.makedirs(<DIRNAME>, exist_ok = True)
    is a good replacement for the custom ensure_dir function above.
    The "exist_ok" keyword is however not available for python 2.7.x.
    '''
