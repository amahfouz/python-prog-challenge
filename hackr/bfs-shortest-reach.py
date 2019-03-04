#!/bin/python

import math
import os
import random
import re
import sys
from collections import deque

# Complete the bfs function below.
def bfs(n, m, edges, s):

    # adjacency list
    adjacency = [ [] for _ in range(n+1)]

    # computed reach 
    reach = [-1 for _ in range(n+1)]
    reach[s] = 0

    # undirected graph - add edge both ways
    for e in edges:
        adjacency[e[0]].append(e[1])
        adjacency[e[1]].append(e[0])

    queue = deque()
    queue.appendleft(s)

    while len(queue) > 0:
        parent = queue.pop()

        # add all unvisited neighbors to next level    
        for neighbor in adjacency[parent]:
            if reach[neighbor] < 0:
               reach[neighbor] = reach[parent] + 1
               queue.appendleft(neighbor) 

    # remove the source from the result as per problem def
    reach.pop(s)
    # there is no node #0 so pop unused element
    reach.pop(0) 
    return [x * 6 if x > 0 else x for x in reach]

if __name__ == '__main__':
    q = int(raw_input())

    for q_itr in xrange(q):
        nm = raw_input().split()

        n = int(nm[0])

        m = int(nm[1])

        edges = []

        for _ in xrange(m):
            edges.append(map(int, raw_input().rstrip().split()))

        s = int(raw_input())

        result = bfs(n, m, edges, s)


        