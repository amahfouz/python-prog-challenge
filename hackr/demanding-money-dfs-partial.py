#!/bin/python
#
# Brute force solution for 
#    https://www.hackerrank.com/challenges/borrowing-money/problem

import math
import os
import re
import sys
import collections

# Result of a single graph component
class Result(object):
    def __init__(self, sum, combinations):
        self.sum = sum
        self.combinations = combinations

# Graph component holding number of nodes and an arbitrary node
class Component(object):
    def __init__(self, size, start):
        self.size = size
        self.start = start

    def __str__(self):
        return str(self.size) + ', ' + str(self.start)

# Breaks a graph into connected components
class Componentizer(object):

    def __init__(self, adjacency, num_nodes):
        self.adjacency = adjacency
        self.num_nodes = num_nodes
        self.visited = [ False for _ in range(num_nodes+1) ]
        self.components = []

    def componentize(self):  
        cur_node = 1
        num_visited = 0
        while True:
            counter = ComponentDfsNodeCount(self.adjacency, self.visited, cur_node)
            self.components.append(Component(counter.count, cur_node))
            num_visited += counter.count
            if num_visited == self.num_nodes:
                break
          
            # find the next starting point
            while cur_node < self.num_nodes and self.visited[cur_node]:
                cur_node += 1

        return self.components

# Performs DFS to count nodes in a graph component
class ComponentDfsNodeCount(object):

    def __init__(self, adjacency, visited, start):
        self.adjacency = adjacency
        self.visited = visited
        self.count = 0
        self.dfs(start)

    def dfs(self, node):    
        if self.visited[node]:
            return
        self.visited[node] = True
        self.count += 1
        for child in self.adjacency[node]:
            self.dfs(child)

# compact representation of an array of booleans
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
    def __init__(self, money, adjacency, component):

        self.money = money
        self.adjacency = adjacency
        self.num_nodes = component.size
        self.visited = [ False for _ in range(len(money)+1)]
        #  included or not in the money sum
        self.included = BitVector()
        self.num_visited = 0
        self.cur_sum = 0

        self.result = Result(0, set())
        self._process(component.start)

    def _process(self, node):
        
        # guard against loops and ensure termination
        if self.visited[node]:
            return

        # first, attempt to include the node 
        can_add_node = self._superhero_present(node)
        
        self._visit(node, can_add_node)

        # visit children recursively
        for child in self.adjacency[node]:
            self._process(child)   

        # now repeat while excluding the node, if not already done 
        if can_add_node:            
            self._include(node, False)
            # visit children again with node unselected
            for child in self.adjacency[node]:
                self._process(child)   
        
        # pop the node off the stack allowing parent to re-iterate
        self._unvisit(node)

    def _visit(self, node, add):
        self.num_visited += 1
        self.visited[node] = True
        if add:
            self._include(node, True)

        # if traversed all nodes check the sum
        if self.num_visited == self.num_nodes and self.cur_sum >= self.result.sum:  
            # reuse set if same result otherwise abandon and create a new set
            new_combinations = self.result.combinations if self.cur_sum == self.result.sum else set()
            new_combinations.add(self.included.to_int())
            self.result = Result(self.cur_sum, new_combinations)

    def _unvisit(self, node):
        self.num_visited -= 1                
        self.visited[node] = False

    def _include(self, node, include):    
        sign = 1 if include else -1 
        self.cur_sum += sign * self.money[node - 1]
        if include:
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

class Solution(object):
    def __init__(self, money, edges):

        num_nodes = len(money)
        # adjacency list
        self.adjacency = [ [] for _ in range(num_nodes + 1)]

        # undirected graph - add edge both ways
        for e in edges:
            self.adjacency[e[0]].append(e[1])
            self.adjacency[e[1]].append(e[0])

        componentizer = Componentizer(self.adjacency, num_nodes)
        components = componentizer.componentize()
        for c in components:
            print str(c)

        total_sum = 0
        num_ways = 1
        for c in components:
            comp = ConnectedComponent(money, self.adjacency, c)
            print comp.result.sum
            total_sum += comp.result.sum
            num_ways *= len(comp.result.combinations)

        print total_sum , num_ways

# main entry point
if __name__ == '__main__':

    nm = raw_input().split()

    n = int(nm[0])

    m = int(nm[1])

    money = map(int, raw_input().rstrip().split())

    roads = []

    for _ in xrange(m):
        roads.append(map(int, raw_input().rstrip().split()))

    sol = Solution(money, roads)

    

