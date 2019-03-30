#!/bin/python

import math

# Implementation range-minimum query segment tree

class SegTree(object):

    def __init__(self, items_array):
        self.items_array = items_array
        num = len(items_array)
        height = int(math.ceil(math.log(num) / math.log(2)))
        num_nodes = 2 * (2 ** height) - 1
        self.tree = [None] * num_nodes 

        self._add_node(0, num - 1, 0)

    def rmq(self, q_start, q_end):
        return self._rmq(0, len(self.items_array) - 1, q_start, q_end, 0)

    def debug(self):
        print self.tree

    def _rmq(self, seg_start, seg_end, q_start, q_end, node_index):
        # segment included in query range
        if q_start <= seg_start and seg_end <= q_end:
            return self.tree[node_index]

        # segment not intersecting query range
        if q_start > seg_end or q_end < seg_start:
            return float("inf")   

        # segment overlaps query range
        mid = SegTree._get_mid(seg_start, seg_end)    

        left = self._rmq(seg_start, mid, q_start, q_end, SegTree._left_of(node_index))
        right = self._rmq(mid + 1, seg_end, q_start, q_end, SegTree._right_of(node_index))
        return min(right, left)

    def _add_node(self, start, end, node_index):
        if start == end:
            item_to_add = self.items_array[start]
            self.tree[node_index] = item_to_add
            return item_to_add

        mid = SegTree._get_mid(start, end)

        left = self._add_node(start, mid, SegTree._left_of(node_index))
        right = self._add_node(mid + 1, end, SegTree._right_of(node_index))
        self.tree[node_index] = min(left, right)

        return self.tree[node_index]

    @staticmethod
    def _left_of(node_index):
        return 2 * node_index + 1

    @staticmethod
    def _right_of(node_index):
        return SegTree._left_of(node_index) + 1

    @staticmethod
    def _get_mid(start, end):
        return start + (end - start) / 2    

######################################################

if __name__ == '__main__':          
    arr = [2, 5, 1, 4, 9 ,3]
    tree = SegTree(arr)
    tree.debug()
    print tree.rmq(3, 5)