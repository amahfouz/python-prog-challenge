'''
Created on Aug 7, 2014

@author: amahfouz
'''

def solveCase():
    x = int(raw_input())
    y = x
    result = 0
    
    while y != 0:
        digit = y % 10
        if digit != 0 and x % digit == 0:
            result = result + 1
        y = y / 10

    print result
        
numCases = int(raw_input())
for case in range(0, numCases):
    solveCase()

