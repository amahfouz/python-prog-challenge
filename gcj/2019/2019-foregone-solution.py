#!/bin/python

n = int(raw_input())

for i in range(n):    
    seq = raw_input()
    
    out1 = ""
    out2 = ""
    
    for c in seq:
        if c == '4':
            out1 += '3'
            out2 += '1'
        else:
            out1 += c
            out2 += '0'

    print "Case #" + str(i+1) + ":", out1, int(out2)    

