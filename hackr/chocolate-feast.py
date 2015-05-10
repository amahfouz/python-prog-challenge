'''
Created on Aug 7, 2014

@author: amahfouz
'''

import math
import sys

def solveCase():
    n, c, m = [int(x) for x in raw_input().split(' ')]
    
    bought = int(math.floor(n/c))
    result = bought
    wrappers = bought
    
    bonus = wrappers / m
    while bonus > 0:
        result = result + bonus
        wrappers = wrappers - m * bonus + bonus
        bonus = wrappers / m
        
    return result    
        
numCases = int(raw_input())
for case in range(0, numCases):
    print solveCase()

