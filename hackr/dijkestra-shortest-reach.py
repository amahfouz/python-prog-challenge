#!/bin/python

import math
import os
import random
import re
import sys
import heapq

# Complete the bfs function below.
def bfs(n, m, edges, s):

    # adjacency list
    adjacency = [ [] for _ in range(n+1)]

    # computed reach 
    reach = [-1 for _ in range(n+1)]
    reach[s] = 0

    # undirected graph - add edge both ways
    for e in edges:
        adjacency[e[0]].append([e[1], e[2]])
        adjacency[e[1]].append([e[0], e[2]])

    heap = []
    heapq.heappush(heap, (0, s))

    while len(heap) > 0:
        entry = heapq.heappop(heap)
        parent = entry[1]

        # iterate over children
        for edge in adjacency[parent]:
            child = edge[0]
            weight = edge[1]
            child_reach = reach[parent] + weight
            
            if reach[child] == -1 or child_reach < reach[child]:
               reach[child] = child_reach
               heapq.heappush(heap, (reach[child], child)) 

    # remove the source from the result as per problem def
    reach.pop(s)
    # there is no node #0 so pop unused element
    reach.pop(0) 
    return reach

if __name__ == '__main__':
    t = int(raw_input())

    for t_itr in xrange(t):
        nm = raw_input().split()

        n = int(nm[0])

        m = int(nm[1])

        edges = []

        for _ in xrange(m):
            edges.append(map(int, raw_input().rstrip().split()))

        s = int(raw_input())

        result = bfs(n, m, edges, s)

        print result


        