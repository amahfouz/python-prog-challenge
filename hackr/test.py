'''
Created on Aug 15, 2014

@author: amahfouz
'''

import bisect

l = [(1, 0), (2, 4), (3, 3), (4, 1), (5, 2)]

bisect.bisect_left(sorted(l), (5, _));