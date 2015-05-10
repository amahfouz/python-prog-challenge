'''
Created on Aug 10, 2014

@author: amahfouz
'''

import bisect

# precompute 100 fibos (more than enough for 10^10
fibos = [0, 1]
for _ in range(0,100):
    l = len(fibos)
    fibos.append(fibos[l - 1] + fibos[l - 2])
    
numCases = int(raw_input())
for case in range(0, numCases):
    candidate = int(raw_input())
    index = bisect.bisect_left(fibos, candidate)
    if (index != len(fibos) and fibos[index] == candidate):
        print "IsFibo"
    else:
        print "IsNotFibo"
        
        
    