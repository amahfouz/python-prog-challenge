'''
Created on Sep 7, 2014

@author: amahfouz
'''

# factorials[i] = the factorial of i
factorials = [1, 1]
divider = 1000000007

def calcFacts():
    for i in range(2, 2000):
        factorials.append(i * factorials[i - 1])

def fact(n):
    return factorials[n]

def solveCase():
    n, m = [int(x) for x in raw_input().split(' ')]
    
    slots = n + m - 1
    ones = m - 1
    
    result = fact(slots) / fact(ones) / fact(slots - ones)
    
    print result % divider

# main

calcFacts()
numCases = int(raw_input())
for case in range(0, numCases):
    solveCase()
