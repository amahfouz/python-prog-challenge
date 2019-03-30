#!/bin/python

import math
import os
import random
import re
import sys
import copy

# Implementation of a 2-D k-D tree and range search

# A point in a 2D plane
class Point:
    def __init__(self, x, y, data):
        self.x = x
        self.y = y
        self.data = data

    def in_rect(self, rect):
        return (self.x >= rect.xmin) and (self.x <= rect.xmax) \
           and (self.y >= rect.ymin) and (self.y <= rect.ymax)

    def __repr__(self):
        return '(' + str(self.x) + ', ' + str(self.y) + ')'

# A rectangle in a 2D plane
class Rect(object):
    def __init__(self, xmin, xmax, ymin, ymax):
        self.xmin = xmin
        self.xmax = xmax
        self.ymin = ymin
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
        return Rect(ninf, inf, ninf, inf)        

# Tree node holding a point and a rectangular 
# range specified by this node
class Node(object):
    def __init__(self, point):
        self.point = point
        self.left = None
        self.right = None 
        self.rect = None

    def is_leaf(self):
        return self.left is None and self.right is None

    @staticmethod
    def debug(node, indent):
        if node is None:
            print ' ' * 2 * indent, "NULL"
            return

        print ' ' * 2 * indent, str(node.point), str(node.rect)
        Node.debug(node.left, indent + 1)
        Node.debug(node.right, indent + 1)

# 2-D K-D tree implementation
class TwoDTree:
    def __init__(self, points):
        self.root = None

        # nodes inserted here only
        for p in points:
            self.root = self._insert(p, self.root, 0)

        # now the tree is fixed so compute ranges
        self._set_ranges()
        
    def debug(self):
        if self.root is None:
            print "Empty Tree"
        else:
            Node.debug(self.root, 0)            

    def _insert(self, point, parent, level):
        if parent is None:
            return Node(point)

        axis = self._axis_for_level(level)

        side = "left" if getattr(point, axis) < getattr(parent.point, axis) else "right"
        next_parent = getattr(parent, side)
        inserted = self._insert(point, next_parent, level + 1)
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
            new_max = getattr(node.point, axis)
            new_rect = Rect.dec_max(rect, axis, new_max)
            self._set_range(node.left, new_rect, level+1)
        
        if not node.right is None:
            new_min = getattr(node.point, axis)
            new_rect = Rect.inc_min(rect, axis, new_min)
            self._set_range(node.right, new_rect, level+1)

    def _axis_for_level(self, level):
        return "x" if level % 2 == 0 else "y"

# finds nodes whose x and y are withing 
# the specified rect and pass them to
# the specified callback function
class RangeSearch:
    def __init__(self, tree, rect, callback):
        self.tree = tree
        self.rect = rect
        self.callback = callback

    # searches for nodes in the given rect
    # reports results in the specified queue
    def find(self):
        self._dfs(self.tree.root)

    def _dfs(self, node):
        if node is None:
            return

        if node.point.in_rect(self.rect):
            self._report(node)  
            self._dfs(node.left)
            self._dfs(node.right)

        else:
            if node.left and node.left.rect.intersects(self.rect):
                self._dfs(node.left)

            if node.right and node.right.rect.intersects(self.rect):
                self._dfs(node.right)

    def _report(self, node):
        self.callback(*[node])
        
# For testing        
def _callback(param):
    print str(param.point)

if __name__ == '__main__':
    points = [Point(1, 2, 0), Point(4, 2, 0), Point(3, 5, 0), Point(4, 0, 0), Point(0, 7, 0), Point(2, 6, 0)]
    tree = TwoDTree(points) 
    tree.debug()
    rect = Rect(0, 4, 0, 0)
    search = RangeSearch(tree, rect, _callback)
    search.find()
    