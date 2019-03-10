#!/bin/python
#
# Brute force solution for 
#    https://www.hackerrank.com/challenges/borrowing-money/problem

import math
import os
import re
import sys
import Queue
import collections

class BitVector(object):
    def __init__(self):
        self._mask = 0

    def set(self, pos):
        self._mask |= 1 << pos

    def unset(self, pos):
        if self.test(pos):
            self._mask ^= 1 << pos    

    def test(self, pos):
        return (self._mask >> pos) & 1

    def to_int(self):
        return self._mask    


# Single connected component of the graph
class ConnectedComponent(object):

    # constructor. Inits adjacency and visited list. Triggers traversal.
    def __init__(self, money, edges):

        # 0-based. Index is one less than node number
        self.money = money

        # adjacency list
        self.adjacency = [ [] for _ in range(len(money) + 1)]

        # undirected graph - add edge both ways
        for e in edges:
            self.adjacency[e[0]].append(e[1])
            self.adjacency[e[1]].append(e[0])

        self.visited = [ False for _ in range(n+1)]
        #  included or not in the money sum
        self.included = BitVector()
        self.numVisited = 0
        self.curSum = 0

        self.Result = collections.namedtuple('Result', 'sum combinations')
        self.result = self.Result(sum=0, combinations=set())
        self._process(1)

    def _process(self, node):
        
        # guard against loops and ensure termination
        if self.visited[node]:
            return

        # first, attempt to include the node 
        canAddNode = self._superhero_present(node)
        
        self._visit(node, canAddNode)

        # visit children recursively
        for child in self.adjacency[node]:
            self._process(child)   

        # now repeat while excluding the node, if not already done 
        if canAddNode:            
            self.include(node, False)
            # visit children again with node unselected
            for child in self.adjacency[node]:
                self._process(child)   
        
        # pop the node off the stack allowing parent to re-iterate
        self._unvisit(node)

    def _visit(self, node, doAdd):
        self.numVisited += 1
        self.visited[node] = True
        if doAdd:
            self.include(node, True)

        # if traversed all nodes check the sum
        if self.numVisited == len(self.money) and self.curSum >= self.result.sum:  
            
            # reuse set if same result otherwise abandon and create a new set
            _new_combinations = self.result.combinations 
                if self.curSum == self.result.sum 
                else set()
            
            _new_combinations.add(self.included.to_int())
            self.result = self.Result(sum=self.curSum, combinations=_new_combinations)

    def _unvisit(self, node):
        self.numVisited -= 1                
        self.visited[node] = False

    def include(self, node, doInclude):    
        sign = 1 if doInclude else -1 
        self.curSum += sign * self.money[node - 1]
        if doInclude:
            self.included.set(node)
        else:
            self.included.unset(node)

    # determines if a superhero is at the given node
    def _superhero_present(self, node):
        # if any neighbor has been visited then superhero skipped town
        for child in self.adjacency[node]:
            if self.included.test(child):
                return False
        return True

# main entry point
if __name__ == '__main__':

    nm = raw_input().split()

    n = int(nm[0])

    m = int(nm[1])

    money = map(int, raw_input().rstrip().split())

    roads = []

    for _ in xrange(m):
        roads.append(map(int, raw_input().rstrip().split()))

    sol = ConnectedComponent(money, roads)

    print sol.result.sum , len(sol.result.combinations)

