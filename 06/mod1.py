# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 20:11:07 2019

@author: JIAMPAN
"""
import random

pwdGenSymbols = "!@#$%^&*()_+-=~`[]\;',./{}|:\"<>?0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

def genPassword(n):
    a = 0
    result = ""
    while a < n:
        result = result + pwdGenSymbols[random.randint(0,len(pwdGenSymbols)-1)]
        a=a+1
    return result
genPassword(12)