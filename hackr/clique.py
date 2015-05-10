'''
Created on Sep 12, 2014

@author: amahfouz
'''
import math

def solveCase():
    n, m = [int(x) for x in raw_input().strip().split(' ')]
    
    lower_bound = 1.0 / (1.0 - (2.0 * m / (n * n * 1.0)))
    
    print int(math.ceil(lower_bound))

# main

numCases = int(raw_input())
for case in range(0, numCases):
    solveCase()