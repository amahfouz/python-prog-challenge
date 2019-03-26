#!/bin/python

import math
import os
import random
import re
import sys
import copy

# Solution for
# https://www.hackerrank.com/challenges/maximizing-mission-points/problem

# A rectangle in a 2D plane
class Rect(object):
    def __init__(self, xmin, ymin, xmax, ymax):
        self.xmin = xmin
        self.ymin = ymin
        self.xmax = xmax
        self.ymax = ymax

    def intersects(self, other):
        if (self.xmax < other.xmin) or (other.xmax < self.xmin) or \
           (self.ymax < other.ymin) or (other.ymax < self.ymin):
           return False
        return True 

    @staticmethod
    def inc_min(original, dim, value):
        rect = copy.copy(original)
        attr = dim + "min"
        setattr(rect, attr, max(value, getattr(rect, attr)))
        return rect

    @staticmethod
    def dec_max(original, dim, value):
        rect = copy.copy(original)
        attr = dim + "max"
        setattr(rect, attr, min(value, getattr(rect, attr)))
        return rect
                
    def __repr__(self):
        return '[ (' + str(self.xmin) + ', ' + str(self.ymin) + ')' \
                +'(' + str(self.xmax) + ', ' + str(self.ymax) + ') ]'

    @staticmethod
    def all_plane():
        inf = float("inf")
        ninf = float("-inf")
        return Rect(ninf, ninf, inf, inf)        

# Tree node holding a city, its point value, a rect
# range specified by this node, and best result that
# is achievable if we start from this node
class Node(object):
    def __init__(self, x, y, z, value):
        self.x = x
        self.y = y
        self.z = z
        self.value = value
        self.left = None
        self.right = None 
        self.rect = None
        self.best = None

    def is_leaf(self):
        return self.left is None and self.right is None

    def in_rect(self, rect):
        return (self.x >= rect.xmin) and (self.x <= rect.xmax) \
           and (self.y >= rect.ymin) and (self.y <= rect.ymax)

    def __cmp__(self, other):
        return self.z - other.z    

    @staticmethod
    def debug(node, indent):
        if node is None:
            print ' ' * 2 * indent, "NULL"
            return

        print ' ' * 2 * indent, '(' + str(node.x) + ', ' + str(node.y) + ')', str(node.rect)
        Node.debug(node.left, indent + 1)
        Node.debug(node.right, indent + 1)

# 2-D K-D tree implementation
class TwoDTree:
    def __init__(self, nodes):
        self.root = None

        # nodes inserted here only
        for n in nodes:
            self.root = self._insert(n, self.root, 0)

        # now the tree is fixed so compute ranges
        self._set_ranges()
        
    def debug(self):
        Node.debug(self.root, 0)            

    def _insert(self, node, parent, level):
        if parent is None:
            return node

        axis = self._axis_for_level(level)
        
        side = "left" if getattr(node, axis) < getattr(parent, axis) else "right"
        next_parent = getattr(parent, side)
        inserted = self._insert(node, next_parent, level + 1)
        setattr(parent, side, inserted)
        return parent

    def _set_ranges(self):
        if self.root is None:
            return
        self._set_range(self.root, Rect.all_plane(), 0)

    # recurses down the tree setting ranges of nodes
    def _set_range(self, node, rect, level):
        node.rect = rect
        axis = self._axis_for_level(level)

        if not node.left is None:
            new_max = getattr(node, axis)
            new_rect = Rect.dec_max(rect, axis, new_max)
            self._set_range(node.left, new_rect, level+1)
        
        if not node.right is None:
            new_min = getattr(node, axis)
            new_rect = Rect.inc_min(rect, axis, new_min)
            self._set_range(node.right, new_rect, level+1)

    def _axis_for_level(self, level):
        return "x" if level % 2 == 0 else "y"

# finds nodes whose x and y are withing 
# the specified rect and collect them

class RangeSearch:
    def __init__(self, tree, rect):
        self.tree = tree
        self.rect = rect
        self.result = []
        self._find()

    # searches for nodes in the given rect
    # reports results in the specified queue
    def _find(self):
        self._dfs(self.tree.root)

    def _dfs(self, node):
        if node is None:
            return

        if node.in_rect(self.rect):
            self.result.append(node)
            self._dfs(node.left)
            self._dfs(node.right)

        else:
            if node.left and node.left.rect.intersects(self.rect):
                self._dfs(node.left)

            if node.right and node.right.rect.intersects(self.rect):
                self._dfs(node.right)
        

# solution:
#
# Construct a 2D tree with the nodes
# For each node
#    Find possible next nodes
#    For each possibility:
#        if the best value has been computed return
#        otherwise recurse 
#
# Once done, find the max among all best values
class Solution(object):
    def __init__(self, nodes, dx, dy):
        self.dx = dx
        self.dy = dy
        self.nodes = nodes

        self.tree = TwoDTree(nodes) 
        Node.debug(self.tree.root, 0)

    def solve(self):
        for node in nodes:
            self._compute_best(node)

        best_best = 0
        for node in nodes:
            if node.best > best_best:
                best_best = node.best

        return best_best


    def _compute_best(self, node):
        if not node.best is None:
            return

        rect = Rect(node.x - self.dx, node.y - self.dy, 
                    node.x + self.dx, node.y + self.dy)
        search = RangeSearch(self.tree, rect)
        
        # find best next step
        best_next = 0
        for next_node in search.result:
            # only allowed to go to a higher z
            if next_node.z < node.z:
                continue
            if next_node == node:
                continue    
            self._compute_best(next_node)
            if next_node.best > best_next:
                best_next = next_node.best
            
        node.best = best_next + node.value

if __name__ == '__main__':
    nD_latD_long = raw_input().split()

    n = int(nD_latD_long[0])

    d_lat = int(nD_latD_long[1])

    d_long = int(nD_latD_long[2])

    nodes = []

    for n_itr in xrange(n):
        latitudeLongitude = raw_input().split()

        latitude = int(latitudeLongitude[0])

        longitude = int(latitudeLongitude[1])

        height = int(latitudeLongitude[2])

        points = int(latitudeLongitude[3])

        # Write Your Code Here

        nodes.append(Node(latitude, longitude, height, points))
    
    solution = Solution(nodes, d_lat, d_long)    
    print solution.solve()




    