'''
Created on Aug 10, 2014

@author: amahfouz
'''
import math
def solveCase():
    cycles = int(raw_input())
    if cycles == 0:
        return 1;

    isOdd = cycles % 2
    if isOdd:
        return (1 << (((cycles + 1) / 2) + 1)) - 2
    else:
        return (1 << ((cycles / 2) + 1)) - 1

#main
numCases = int(raw_input())
for _ in range(0, numCases):
    print int(solveCase())
    