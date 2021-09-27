#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 27 11:08:49 2021

@author: zhanghanqing
"""

def gcd(a, b):
    """
    a, b: two positive integers
    Returns the greatest common divisor of a and b
    """
    #YOUR CODE HERE
    if b == 0:
       return a
    else:
       return gcd(b,a%b)
    