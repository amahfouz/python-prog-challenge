'''
Created on Sep 21, 2014

@author: amahfouz
'''

import operator

def solveCase():
    n = int(raw_input())
    denom = [1, 2, 5, 10]
    values = [int(x) for x in raw_input().strip().split(' ')]
    
    total = sum(map(operator.mul, denom, values))
    
    for tens in xrange(values[3], -1, -1)

# main

numCases = int(raw_input())
for case in range(0, numCases):
    solveCase()