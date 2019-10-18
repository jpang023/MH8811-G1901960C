# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 20:11:07 2019

@author: JIAMPAN
"""
import mod1

n=input("What is the length of your password:")
try:
    num = int(n)
    print(mod1.genPassword(num))
except:
    print("Please type a number")
    