#!/usr/bin/python
# -*- coding: utf-8 -*-
##########################################################################################
# adopted by: Nikolas Schnellbaecher
# contact: khx0@posteo.net
# date: 2021-03-24
# file: natural_sort.py
##########################################################################################

import re

def natural_keys(key):
    """
    Natural keys for natural order list sorting
    :param key: Input key for sorting criteria.
    :return: Natural (ordered) key.
    Usage:
    a_list.sort(key=natural_keys), where a_list is a given (potentially) unsorted list
    """
    unify = lambda x: int(x) if x.isdigit() else x.lower()
    return [unify(c) for c in re.split(r'[+-]?([0-9]+(?:[.][0-9]*)?|[.][0-9]+)', key)]

def natural_sort(l):
    """
    Natural sorting algorithm. Sorts a given list l in human order.
    :param l: (Potentially) Unsorted input list.
    :return:  Naturally sorted list.
    """
    unify = lambda x: int(x) if x.isdigit() else x.lower()
    natural_keys = lambda key: [unify(c) for c in re.split(r'[+-]?([0-9]+(?:[.][0-9]*)?|[.][0-9]+)', key)]
    return sorted(l, key=natural_keys)

if __name__ == '__main__':

    ###################################################
    # USAGE INSTRUCTIONS
    #
    # --- Method A ---
    # sorted_list = natural_sort(input_list)
    #
    # --- Method B ---
    # a_list.sort(key = natural_key)
    #
    ####################################################

    pass