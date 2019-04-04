#!/usr/bin/python
# -*- coding: utf-8 -*-
##########################################################################################
# author: Nikolas Schnellbaecher
# contact: khx0@posteo.net
# date: 2019-04-04
# file: run_versions_python2.py
##########################################################################################

import sys
import os
import datetime

now = datetime.datetime.now()
now = "{}-{}-{}".format(now.year, str(now.month).zfill(2), str(now.day).zfill(2))

BASEDIR = os.path.dirname(os.path.abspath(__file__))
RAWDIR = os.path.join(BASEDIR, 'raw')
OUTDIR = os.path.join(BASEDIR, 'out')

if __name__ == '__main__':

    outfilename = "python2_versions_as_of_" + now + ".txt"

    cmd = "python versions.py &> " + outfilename
    os.system(cmd)

    cmd = "python --version"
    os.system(cmd)

    cmd = "which python"
    os.system(cmd)
