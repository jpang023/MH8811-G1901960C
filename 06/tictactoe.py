# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 20:35:21 2019

@author: JIAMPAN
"""

def TicTacDraw(board):
    icount = 0
    for i in board:
        row=""
        jcount = 0
        for j in i:
            if j == 0:
                row = row + "0"
            elif j == 1:
                row = row + "X"
            elif j == 2:
                row = row + " "
            jcount = jcount +1
            if jcount < len(i):
                row = row + "|"
        print(row)
        icount = icount +1
        if icount != len(board):
            print("-"*(len(board)*2 -1))
#TicTacDraw([[0,1,2,0],[2,0,0,1],[1,1,2,0],[2,1,2,0]])