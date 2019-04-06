#!/bin/python

n = int(raw_input())

for i in range(n):
    ignored = raw_input()
    seq = raw_input()
    
    rev = ""
    
    for c in seq:
        rev += ('S' if c == 'E' else 'E')
        
    print "Case #" + str(i+1) + ":", rev    

