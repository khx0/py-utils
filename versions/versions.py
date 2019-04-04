#!/usr/bin/python
# -*- coding: utf-8 -*-
##########################################################################################
# author: Nikolas Schnellbaecher
# contact: khx0@posteo.net
# date: 2019-04-04
# file: versions.py
##########################################################################################

import sys
print("Python sys.version = ", sys.version_info)

import platform
print("platform.python_version() =", platform.python_version())

try:
    import numpy as np
    print("Numpy version = ", np.__version__)
except ImportError:
    print("Error: Numpy not installed")

try:
    import scipy
    print("Scipy version = ", scipy.__version__)
except ImportError:
    print("Error: Scipy not installed")

try:
    import matplotlib as mpl
    print("Matplotlib version = ", mpl.__version__)
except ImportError:
    print("Error: Matplotlib not installed")

try:
    import torch
    print("Torch version = ", torch.__version__)
except ImportError:
    print("Error: torch not installed")

try:
    import torchvision
    print("Torchvision version = ", torchvision.__version__)
except ImportError:
    print("Error: torchvision not installed")

try:
    import sklearn
    print("scikit-learn version =", sklearn.__version__)
except ImportError:
    print("Error: scikit-learn not installed")

try:
    import skimage
    print("scikit-image version =", skimage.__version__)
except ImportError:
    print("Error: scikit-image not installed")

try:
    import PyQt5
    from PyQt5.QtCore import QT_VERSION_STR
    print("PyQt5 version = ", QT_VERSION_STR)
except ImportError:
    print("Error: PyQt5 not installed.")
