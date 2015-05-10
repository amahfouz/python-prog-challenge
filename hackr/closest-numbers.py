'''
Created on Aug 15, 2014

@author: amahfouz
'''

n = int(raw_input())
a = sorted(map(int, raw_input().strip().split(" ")))

diff = [abs(a[i] - a[i - 1]) for i in range(1, len(a))]
min_diff = min(diff)

result = []
for i, d in enumerate(diff):
    if d == min_diff:
        result.append(a[i])
        result.append(a[i + 1])

for r in result: print r,
