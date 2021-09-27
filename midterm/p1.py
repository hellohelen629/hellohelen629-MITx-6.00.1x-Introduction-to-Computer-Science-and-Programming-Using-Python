#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 27 09:37:16 2021

@author: zhanghanqing
"""

def isMyNumber(x):
    secret = 1000
    if x < secret:
        return -1
    elif x == secret:
        return 0
    else:
        return 1

def jumpAndBackpedal(isMyNumber):
    '''
    isMyNumber: Procedure that hides a secret number. 
     It takes as a parameter one number and returns:
     *  -1 if the number is less than the secret number
     *  0 if the number is equal to the secret number
     *  1 if the number is greater than the secret number
 
    returns: integer, the secret number
    ''' 
    guess = 1
    while True:
        if isMyNumber(guess) == 0:
           return guess
           break
        elif isMyNumber(guess) == -1:
            guess += 1
        elif isMyNumber(guess) == 1:
            guess -= 1
    