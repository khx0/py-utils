#!/usr/bin/python
# -*- coding: utf-8 -*-
##########################################################################################
# author: Nikolas Schnellbaecher
# contact: khx0@posteo.net
# date: 2018-07-12
# file: versions.py
##########################################################################################

from subprocess import call
call("python --version", shell = True)

import sys
print "Python sys.version = ", sys.version_info

import numpy as np
print "Numpy version = ", np.__version__

import scipy
print "Scipy version = ", scipy.__version__

import matplotlib as mpl
print "Matplotlib version = ", mpl.__version__

import torch
print "Torch version = ", torch.__version__

import torchvision
print "Torchvision version = ", torchvision.__version__