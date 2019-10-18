# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 20:11:07 2019

@author: JIAMPAN
"""
import random

pwdGenSymbols = "!@#$%^&*()_+-=~`[]\;',./{}|:\"<>?"
pwdGennum ="0123456789"
pwdGencharsu ="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
pwdGencharsl ="abcdefghijklmnopqrstuvwxyz"
pwdGenFull=pwdGenSymbols+pwdGennum+pwdGencharsu+pwdGencharsl

def genPassword(n):
    a = 0
    result = ""
    result = result + pwdGenSymbols[random.randint(0,len(pwdGenSymbols)-1)]
    result = result + pwdGennum[random.randint(0,len(pwdGennum)-1)]
    result = result + pwdGencharsu[random.randint(0,len(pwdGencharsu)-1)]
    result = result + pwdGencharsl[random.randint(0,len(pwdGencharsl)-1)]
    while a < n - 4:
        result = result + pwdGenFull[random.randint(0,len(pwdGenFull)-1)]
        a=a+1
    return result
genPassword(12)