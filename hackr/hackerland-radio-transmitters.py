#!/bin/python

import math
import os
import random
import re
import sys

def count_radio_transmitters(houses, distance):
    houses.sort()

    num_radios = 0
    index_to_cover = 0
    while index_to_cover < len(houses):
        
        # skip all houses within range to find site 
        next = index_to_cover + 1
        while next < len(houses) and \
            houses[next] - houses[index_to_cover] <= distance:
            next += 1   

        # add radio site at next - 1
        num_radios += 1

        # skip covered houses and find next house to cover
        index_to_cover = next
        while index_to_cover < len(houses) \
            and houses[index_to_cover] - houses[next - 1] <= distance:
            index_to_cover += 1

    return num_radios

if __name__ == '__main__':
    print count_radio_transmitters([7, 2, 4, 6, 5, 9, 12, 11], 2)