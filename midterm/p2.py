#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 27 10:10:02 2021

@author: zhanghanqing
"""

d = {0: 9, 9: 9, 5: 9}
def dict_invert(d):
    '''
    d: dict
    Returns an inverted dictionary according to the instructions above
    '''
    # Your code here

    d_inv = {}
    for key, value in d.items():
        d_inv.setdefault(value, list()).append(key)
    for val in d_inv.values():
        val.sort()

    return d_inv