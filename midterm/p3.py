#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 27 10:21:49 2021

@author: zhanghanqing
"""

def dict_invert(d):
    '''
    d: dict
    Returns an inverted dictionary according to the instructions above
    '''
    # Your code here
    inverse = {}
    for elm in d.keys():
        if d[elm] in inverse:
            inverse[d[elm]].append(elm)
        else:
            inverse[d[elm]] = [elm]
    for val in inverse.values():
        val.sort()
    return inverse
    
        
    