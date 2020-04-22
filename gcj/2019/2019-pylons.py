#!/bin/python

def translate(pairs, r):
    result = []
    for pair in pairs:
        result.append((pair[0] + r, pair[1]))
    return result

_2x5 = [(2, 3), 
        (1, 1), 
        (2, 4),
        (1, 2), 
        (2, 5), 
        (1, 3),
        (2, 1),
        (1, 5),
        (2, 2),
        (1, 4)]

_3x5 = [ (2,2), (1, 4), (3,5), (2,3), (1,1), (3,2), (1,3), (3,4), (2,5), (3,3), (2,1), (1,5), (3,1), (2,4), (1,2)]

_4x5 = _2x5 + translate(_2x5, 2)

_5x5 = _3x5 + translate(_2x5, 3)

_3x4 = [(1,1), (2, 3), (3,1), (1,2), (2,4), (3,2), (1,3), (3,4), (2,2), (1,4), (3,3), (2,1)]

_4x4 = [(2,2), (4,3), (1,4), (3,1), (1, 2), (4,4), (3,2), (1,3), (3,4), (4,1), (3,3), (2,1), (4,2), (2,3), (1,1)]

sol = [[None, None, None, _2x5],
       [None, None, _3x4, _3x5],        
       [None, None, _4x4, _4x5],        
       [None, None, None, _5x5]]        

def solve(r, c):
    rev = False
    if (r > c):
        rev = True        
        r, c = c, r

    solution = sol[r - 2][c - 2]
    if solution is None:
        return None

    return transpose(solution) if rev else solution    

def transpose(pairs):
    result = []
    for pair in pairs:
        result.append((pair[1], pair[0]))
    return result    


###############################

if __name__ == '__main__':        

    n = int(raw_input())
    for i in range(n):    
        size = map(int, raw_input().rstrip().split()) 
        r = size[0]
        c = size[1]
        result = solve(r, c)
        if result is None:
            print "Case #" + str(i+1) + ": IMPOSSIBLE"
        else:
            print "Case #" + str(i+1) + ": POSSIBLE"
            for p in result:
                print p[0], p[1]