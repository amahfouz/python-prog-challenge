#!/bin/python
#
# Brute force solution for 
#    https://www.hackerrank.com/challenges/borrowing-money/problem

# A more efficient solution:
# https://www.hackerrank.com/rest/contests/master/challenges/borrowing-money/hackers/ivanbessonov/download_solution?primary=true
# 

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

# An edge holding low/high ordinal nodes and a mask combining them
class Edge(object):

    def __init__(self, node1, node2):
        self.mask = 1<<node1 | 1<<node2
        if node1 > node2:
            node1, node2 = node2, node1
        self.low_node = node1
        self.high_node = node2
        self.low_node_mask = 1 << node1

    # edges with smaller mask come first 
    def __cmp__(self, other):
        return other.mask - self.mask

    def __str__(self):        
        return str(self.high_node) + ' ' + str(self.low_node)

    def __repr__(self):        
        return str(self.high_node) + ' ' + str(self.low_node)

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
    def __init__(self, money, edge_mask_objs, component):

        self.component = component
        self.money = money

        result = Result(-1, set())

        # try every node inclusion combination using a bit mask
        # the mask corresponds to positions of nodes in their component
        short_mask = 0
        num_nodes = len(component.nodes)
        for short_mask in reversed(range(1 << num_nodes)):   

            # if short_mask % 300000 == 0:
            #     print "Processed ", short_mask 

            # bits in the short mask correspond to node positions in
            # the component, whereas we need node positions in the
            # whole graph to match the indices in the edges list and
            # also to index into the money array
            included = self._calc_long_mask(short_mask)
            valid_combination = True
            for edge in edge_mask_objs:
                # check if there is any possibility of overlap
                # edge masks are sorted, so we can skip the rest
                # if (edge.low_node_mask > included):
                #     break

                # check if both ends of an edge are included
                if (edge.mask & included) ^ edge.mask == 0:
                    valid_combination = False

                    # two cases
                    # if we hit combination 01001000
                    # then skip all up to   01001111
                    # and continue at       01010000 
                    # OR if we hit combination 0011100
                    # then skip all up to      0011111
                    # and continue at          0100000
                    # In both cases, set all lower bits up
                    # to the low_node and then add 1 later

                    # if included > 10000:
                    #     for pos in range(edge.low_node):
                    #         included |= (1 << pos)

                    #     short_mask = self._calc_short_mask(included)                        
                    break
            
            # all edge masks pass
            if valid_combination:
                sum = self._calculate_sum(included, money)
                if sum >= result.sum:
                    # reuse set if same result otherwise abandon and create a new set
                    new_combinations = result.combinations if sum == result.sum else set()
                    new_combinations.add(included)
                    result = Result(sum, new_combinations)

            # add 1 in all cases        
            # short_mask += 1

        self.result = result    

    def _calc_short_mask(self, long_mask):
        short_mask = 0
        for i in range(len(self.component.nodes)):
            if long_mask & (1 << self.component.nodes[i]):
                short_mask |= (1 << i)

        return short_mask

    def _calc_long_mask(self, short_mask):
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

        # print "Num components = ", len(components)
        
        # bit mask for each pair of nodes joined by an edge
        edge_masks = []
        for e in edges:
            edge_masks.append(Edge(e[0], e[1]))

        # smaller masks first as their bits change more 
        # often while iterating over all combinations
        edge_masks.sort()    

        total_sum = 0
        num_ways = 1
        for i in range(len(components)):
            c = components[i]
            # print "Processing component ", i, " whose size is ", c.size()
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

    

