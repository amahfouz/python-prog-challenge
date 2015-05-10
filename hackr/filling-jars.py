'''
Created on Aug 10, 2014

@author: amahfouz
'''

import sys
import math

nAndM = sys.stdin.readline().split()
n = int(nAndM[0])
m = int(nAndM[1])

sum = 0;
for x in range(0, m):
    op = sys.stdin.readline().split()
    sum = sum + (int(op[1]) - int(op[0]) + 1) * int(op[2])
        
# compute average

print int(math.floor(sum / float(n)))        
    