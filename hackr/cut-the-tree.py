'''
Created on Aug 12, 2014

@author: amahfouz
'''

import sys

def subtreeSum(index):
    vertex = v[index]
    if vertex['visited']:
        return 0;
    
    vertex['visited'] = True
    children = vertex['children']
    value = vertex['value']
    result = value 
    if len(children) !=  0:
        result = result + sum(map(subtreeSum, children))
    vertex['sum'] = result
    
    print index
    
    return result

# main entry point

n = int(raw_input())

# entry for each node containing the value, list of children, parent, and sub tree sum
v = [{"children":[],  "value": int(v), "sum": 0, "visited": False} for v in raw_input().split(' ')]
# read n-1 lines and build the tree
for _ in xrange(0, n - 1):
    v1, v2 = [int(x) - 1 for x in raw_input().split(' ')]
    v[v1]['children'].append(v2)
    v[v2]['children'].append(v1)

# compute value of each subtree starting at root

v[0]['sum'] = subtreeSum(0)

print v[0]['sum']

# compute best edge

minDiff = 100000000000
for vertex in v:    
    for child in vertex['children']:
        childSum = v[child]['sum']
        diff = abs(v[0]['sum'] - childSum - childSum)
        if (diff < minDiff):
            minDiff = diff

print minDiff   
    
    
    