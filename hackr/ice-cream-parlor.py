'''
Created on Aug 14, 2014

@author: amahfouz
'''

import bisect

def bin_search(a, x, lo):
    i = bisect.bisect_left(a, x, lo)
    if i != len(a) and a[i] == x:
        return i
    else:
        return -1

def solve_case():
    m = int(raw_input())
    n = int(raw_input())
    ints = map(int, raw_input().strip().split(" "))
    sorted_pairs = sorted([(x, i) for i, x in enumerate(ints)])
    idxs = [i for (v, i) in sorted_pairs]
    vals = [v for (v, i) in sorted_pairs]
    
    #print sorted_pairs
    
    for (sorted_idx, val) in enumerate(vals):
        other_sorted_idx = bin_search(vals, m - val, sorted_idx + 1)
        if (other_sorted_idx >= 0):
            first = idxs[sorted_idx] + 1
            second = idxs[other_sorted_idx] + 1
            print min(first, second), max(first, second)
            return
        

# main entry

num_cases = int(raw_input())
for case in range(0, num_cases):
    solve_case()
