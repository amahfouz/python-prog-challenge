#!/bin/python

import math

# Implementation range-minimum query segment tree

class SegTree(object):

    def __init__(self, items_array):
        self.items_array = items_array
        num = len(items_array)
        height = int(math.ceil(math.log(num) / math.log(2)))
        num_nodes = 2 * (2 ** height) - 1

        # holds the min of the segment and the index of the
        # min value in the original array
        self.tree = [(None, None)] * num_nodes 

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
            return -1, float("inf")

        # segment overlaps query range
        mid = SegTree._get_mid(seg_start, seg_end)    

        left = self._rmq(seg_start, mid, q_start, q_end, SegTree._left_of(node_index))
        right = self._rmq(mid + 1, seg_end, q_start, q_end, SegTree._right_of(node_index))

        return left if (left[1] < right[1]) else right

    def _add_node(self, start, end, node_index):
        if start == end:
            item_to_add = self.items_array[start]
            self.tree[node_index] = (start, item_to_add)
            return (start, item_to_add)

        mid = SegTree._get_mid(start, end)

        l_index, left = self._add_node(start, mid, SegTree._left_of(node_index))
        r_index, right = self._add_node(mid + 1, end, SegTree._right_of(node_index))
        
        result = (l_index, left) if left < right else (r_index, right)
        self.tree[node_index] = result

        return result

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

class Solution(object):

    def __init__(self, buildings):
        self.buildings = buildings
        self.tree = SegTree(buildings)

    def solve(self):
        return self._solve(0, len(self.buildings) - 1)

    def _solve(self, start, end):
        print start, end
        if end < start or start < 0 or end >= len(self.buildings):
            return 0

        if (start == end):
            return self.buildings[start] 

        (min_index, min_val) = self.tree.rmq(start, end)   

        base_rect = min_val * (end - start + 1)
        left_sol = self._solve(start, min_index - 1)
        right_sol = self._solve(min_index + 1, end)

        return max(base_rect, max(left_sol, right_sol))

######################################################            

if __name__ == '__main__':          
    arr = [1,2,3,4,5]
    sol = Solution(arr)
    print sol.solve()