
# Solution taken from https://pastebin.com/1R543whN

#
# The entry dp[i][j] holds the solution for the sub-problem 
# where the total set is only the first i integers and j of
# those have been picked for Li
# 
# Example, for the set {1, 6, 7, 12, 13 }
#
# The filled dp matrix will look like:
#
#      |  0     1     2     3     4    5
#  ---------------------------------------
#  0   |  x     x     x     x     x    x
#  1   |  x     x     x     x     x    x
#  2   |  x     5     x     x     x    x
#  3   |  x     11    7     x     x    x
#  4   |  x     23    24    22    x    x
#  5   |  x     35
#  
