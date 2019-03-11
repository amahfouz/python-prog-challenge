#!/bin/python
#
# Brute force solution for 
#    https://www.hackerrank.com/challenges/borrowing-money/problem

import math
import os
import re
import sys
import collections
from bisect import bisect_left

#
# Break the graph into connected components
# For every component:
#   For every bit mask for its nodes
#       For every edge mask
#           if mask passes
#               calculate money
#               check if larger than or equal max
# Combine all component sums
#

# Result of a single graph component
class Result(object):
    def __init__(self, sum, combinations):
        self.sum = sum
        self.combinations = combinations

# Graph component holding sorted list of nodes
class Component(object):
    def __init__(self, nodes):
        self.nodes = nodes
        self.nodes.sort()
    #     self.node_for_pos = {}
    #     for i in range(len(nodes)):
    #         self.node_for_pos[nodes[i]] = i

    def size(self):
        return len(self.nodes)

    # def node_for(self, pos):
    #     return self.node_for_pos[node]

    def __str__(self):
        return str(self.nodes)

# Breaks a graph into connected components
class Componentizer(object):

    def __init__(self, adjacency):
        self.adjacency = adjacency
        self.visited = [ False for _ in range(len(adjacency)) ]
        self.components = []

    def componentize(self):  
        cur_node = 0
        num_visited = 0
        while True:
            traversal = ComponentDfsTraversal(self.adjacency, self.visited, cur_node)
            self.components.append(Component(traversal.nodes))
            num_visited += len(traversal.nodes)
            if num_visited == len(self.adjacency):
                break
          
            # find the next starting point
            while cur_node < len(self.adjacency) and self.visited[cur_node]:
                cur_node += 1

        return self.components

# Performs DFS to count nodes in a graph component
class ComponentDfsTraversal(object):

    def __init__(self, adjacency, visited, start):
        self.adjacency = adjacency
        self.visited = visited
        self.nodes = []
        self.dfs(start)
        # now all are visited

    def dfs(self, node):    
        if self.visited[node]:
            return
        self.visited[node] = True
        self.nodes.append(node)
        for child in self.adjacency[node]:
            self.dfs(child)

# Single connected component of the graph
class ConnectedComponent(object):

    # constructor. Inits adjacency and visited list. Triggers traversal.
    def __init__(self, money, edge_masks, component):

        self.component = component
        self.money = money

        result = Result(-1, set())

        # try every node inclusion combination using a bit mask
        # the mask corresponds to positions of nodes in their component
        for short_mask in range(0, 1 << len(component.nodes)):   

            if short_mask % 300000 == 0:
                print "Processed 300K ", short_mask / 300000

            # bits in the short mask correspond to node positions in
            # the component, whereas we need node positions in the
            # whole graph to match the indices in the edges list and
            # also to index into the money array
            included = self._calc_mask(short_mask)
            valid_combination = True
            for mask in edge_masks:
                # check if both ends of an edge are included
                if (mask & included) ^ mask == 0:
                    valid_combination = False
                    break
            # all edge masks pass
            if valid_combination:
                sum = self._calculate_sum(included, money)
                if sum >= result.sum:
                    # reuse set if same result otherwise abandon and create a new set
                    new_combinations = result.combinations if sum == result.sum else set()
                    new_combinations.add(included)
                    result = Result(sum, new_combinations)
        
        self.result = result    

    def _calc_mask(self, short_mask):
        long_mask = 0
        pos = 0
        while short_mask != 0:
            if short_mask &1:
                node_index = self.component.nodes[pos]
                long_mask |= (1 << node_index)
            pos += 1
            short_mask >>= 1
        return long_mask

    def _calculate_sum(self, long_mask, money):
        sum = 0
        pos = 0
        while long_mask != 0:
            if long_mask & 1:
                sum += money[pos]
            pos += 1
            long_mask >>= 1
        return sum

class Solution(object):
    def __init__(self, money, edges):

        num_nodes = len(money)
        # adjacency list
        self.adjacency = [ [] for _ in range(num_nodes)]

        # undirected graph - add edge both ways 
        # while making node numbers 0-based
        
        for e in edges:
            e[0] -= 1
            e[1] -= 1
            self.adjacency[e[0]].append(e[1])
            self.adjacency[e[1]].append(e[0])

        componentizer = Componentizer(self.adjacency)
        components = componentizer.componentize()

        print "Num components = ", len(components)
        
        # bit mask for each pair of nodes joined by an edge
        edge_masks = []
        for e in edges:
            edge_masks.append(1<<e[0] | 1<< e[1])

        total_sum = 0
        num_ways = 1
        for i in range(len(components)):
            c = components[i]
            print "Processing component ", i, " whose size is ", c.size()
            comp = ConnectedComponent(money, edge_masks, c)
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

    

