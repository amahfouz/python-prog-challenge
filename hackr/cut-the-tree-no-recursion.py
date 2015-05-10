'''
Created on Aug 12, 2014

@author: amahfouz
'''

def computeSums():
    # DFT with two stacks
    
    firstStack = [0]
    secondStack = []
    
    while len(firstStack) != 0:
        topIndex = firstStack.pop()
        topRecord = v[topIndex]
        topRecord['visited'] = True
        secondStack.append(topIndex)
        firstStack.extend([child for child in topRecord['children'] if not v[child]['visited']])
                
    # Now nodes are popped from second stack in post order    
    while len(secondStack) != 0:
        index = secondStack.pop()
        childRecord = v[index]
        childRecord['sum'] = childRecord['value'] + sum(map(lambda i : v[i]['sum'], childRecord['children']))
    
# main entry point

n = int(raw_input())

# entry for each node containing the value, list of children, parent, and sub tree sum
v = [{"children":[],  "value": int(v), "sum": 0, "visited": False} for v in raw_input().split(' ')]
# read n-1 lines and build the tree
for _ in xrange(0, n - 1):
    v1, v2 = [int(x) - 1 for x in raw_input().split(' ')]
    v[v1]['children'].append(v2)
    v[v2]['children'].append(v1)

# compute value of each subtree using post order DFT

computeSums()

# for every vertex, try every edge (child) and get the min of the min

print min([min(map(lambda child: abs(v[0]['sum'] - 2 * v[child]['sum']), vertex['children'])) for vertex in v])    

   
    
    
    