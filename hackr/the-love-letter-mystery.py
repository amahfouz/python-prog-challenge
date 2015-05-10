'''
Created on Aug 15, 2014

@author: amahfouz
'''

def solve_case():
    s = raw_input().strip()
    l = len(s)
    print sum([abs(ord(s[i]) - ord(s[l - i - 1])) for i in range(0, l / 2)])

num_cases = int(raw_input())
for case in range(0, num_cases):
    solve_case()
