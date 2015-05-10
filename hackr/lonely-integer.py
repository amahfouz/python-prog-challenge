'''
Created on Aug 14, 2014

@author: amahfouz
'''

def lonelyinteger(a):
    answer = 0
    numMap = dict((a.count(i), i) for i in a)
    return numMap[1] 

a = input()
b = map(int, raw_input().strip().split(" "))
print lonelyinteger(b)
