#!/usr/bin/python
# -*- coding: utf-8 -*-
##########################################################################################
# author: Nikolas Schnellbaecher
# contact: khx0@posteo.net
# date: 2019-05-24
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

    ensure_dir(RAWDIR) # alternatively use: os.makedirs(RAWDIR, exist_ok = True)
    ensure_dir(OUTDIR) # alternatively use: os.makedirs(OUTDIR, exist_ok = True)

    dirname_with_timestamp = "data_" + now
    ensure_dir(dirname_with_timestamp)

    '''
    Using python >3.5 os.makedirs(<DIRNAME>, exist_ok = True)
    is a good replacement for the custom ensure_dir function above.
    The "exist_ok" keyword is however not available for python 2.7.x.
    '''
    
    #######################################################
    # os.path.dirname and os.path.basename example usage
    
    # set up a longer dummy path
    pathToFile = 'dirA/dirB/dirC'
    os.makedirs(pathToFile, exist_ok = True)
    
    # Let's assume that dirC contains some important file.
    # Then it is often useful, to have access to the two
    # variables basedir and basename as illustrated below.
    basedir = os.path.dirname(pathToFile)
    basename = os.path.basename(pathToFile)
    
    print("basedir =", basedir)
    print("basename =", basename)
    #######################################################