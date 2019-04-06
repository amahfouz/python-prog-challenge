#!/bin/python

def solve(arr):

    num_ways = 0
    # each element is a pair of (height, count)
    stack = []
    for cur_height in arr:
        while len(stack) and cur_height > stack[-1][0]:
            pair = stack.pop()
            count = pair[1]
            num_ways += count * (count - 1)

        if len(stack) == 0 or stack[-1][0] > cur_height:
            stack.append([cur_height, 1])
            continue

        top = stack[-1]
        if top[0] != cur_height:
            raise "Not same height!"
        top[1] += 1

    while len(stack):
        pair = stack.pop()  
        count = pair[1]
        num_ways += count * (count - 1)

    return num_ways


if __name__ == '__main__':        
    f = open('input03.txt', 'r')  

    arr_count = int(f.readline())
    print "reading"
    arr = map(int, f.readline().rstrip().split())
    print "read"
    result = solve(arr)

    print result