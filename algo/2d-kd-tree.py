#!/bin/python

import math
import os
import random
import re
import sys

# Implementation of a 2-D k-D tree

class Point:
    def __init__(self, x, y, data):
        self.x = x
        self.y = y
        self.data = data

    def in_range(self, origin, dx, dy):
        return (self.x <= origin.x + dx) and (self.y <= origin.y + dy)

    def __repr__(self):
        return '(' + str(self.x) + ', ' + str(self.y) + ')'

class Node(object):
    def __init__(self, point):
        self.point = point
        self.left = None
        self.right = None 

    def is_leaf():
        return self.left is None and self.right is None

    @staticmethod
    def debug(node, indent):
        if node is None:
            print ' ' * 2 * indent, "NULL"
            return

        print ' ' * 2 * indent, str(node.point)
        Node.debug(node.left, indent + 1)
        Node.debug(node.right, indent + 1)

class TwoDTree:
    def __init__(self, points):
        self.root = None
        for p in points:
            self.root = self._insert(p, self.root, 0)
        
    def debug(self):
        if self.root is None:
            print "Empty Tree"
        else:
            Node.debug(self.root, 0)            

    def _insert(self, point, parent, level):
        if parent is None:
            return Node(point)

        dim = "x" if level % 2 == 0 else "y"

        side = "left" if getattr(point, dim) < getattr(parent.point, dim) else "right"
        next_parent = getattr(parent, side)
        inserted = self._insert(point, next_parent, level + 1)
        setattr(parent, side, inserted)
        return parent

    # finds nodes whose x and y are withing no more 
    # than dx and dy from the specified point
    # class RangeSearch:
    #     def __init__(self, tree, point, callback, dx, dy):
    #         self.tree = tree
    #         self.point = point
    #         self.callback = callback
    #         self.dx = dx
    #         self.dy = dy

    #     # searches for nodes less than or equal the upper bound point
    #     # reports results in the specified queue
    #     def find(self):
    #         self._bfs(self.tree.root)

    #     def _bfs(self, node):
    #         if node is None:
    #             return

    #         fully_contained = node.point.in_range(self.point, self.dx, self.dy)
    #         if node.is_leaf() and fully_contained:
    #             self._report(node)
            

    #     def _report(self, node):
    #         self.callback(*[node])

    #     def _report_all(self, node):
    #         if node is None:
    #             return
    #         self._report(node)
    #         self._report_all(node.left)
    #         self._report_all(node.right)

        


if __name__ == '__main__':
    points = [Point(1, 2, 0), Point(4, 2, 0), Point(3, 5, 0), Point(4, 0, 0), Point(0, 7, 0), Point(2, 6, 0)]
    tree = TwoDTree(points) 
    tree.debug()