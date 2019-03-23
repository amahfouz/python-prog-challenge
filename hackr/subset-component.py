#!/bin/python

import math
import os
import random
import re
import sys

NUM_BITS = 64
def find_connected_components(items):
    num_items = len(items)
    num_combinations = 1 << num_items
    all_combinations = range(num_combinations)

    # graph components for each subset
    components = [[] for _ in all_combinations] 

    # bit mask specifying which items is included
    # in the subset under consideration
    for combination in all_combinations:
        comps_for_comb = components[combination]
        for bit in range(num_items):
            # if the item is included
            if combination & (1 << bit):
                item_to_include = items[bit]
                item_added = False

                # find a component that intersects the item
                for i in range(len(comps_for_comb)):
                    if comps_for_comb[i] & item_to_include:
                        comps_for_comb[i] |= item_to_include
                        item_added = True
                        break
                # if no intersection add a new component
                if not item_added:
                    comps_for_comb.append(item_to_include)
              
    # count the components for each combination
    total_num_components = 0
    for combination in all_combinations:

        # count of nodes that are connected to at least 
        # one other node (not a component on their own)
        num_non_island_nodes = 0

        # number of masks that have a single 1 bit 
        masks_with_single_one = 0
        comp_list = components[combination]
        for component in comp_list:
            num_ones = bin(component).count("1")
            # a mask with a single set bit is an islan node
            if num_ones > 1:
                num_non_island_nodes += num_ones
            else:
                masks_with_single_one += 1

        num_comps_for_comb = (len(comp_list) - masks_with_single_one) + (64 - num_non_island_nodes)
        total_num_components += num_comps_for_comb

    return total_num_components


if __name__ == '__main__':
    find_connected_components([2, 5, 9])