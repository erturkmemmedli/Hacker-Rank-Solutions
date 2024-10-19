# Ema's Supercomputer


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'twoPluses' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING_ARRAY grid as parameter.
#

def twoPluses(grid):
    # Write your code here
    all_pluses = []
    m, n = len(grid), len(grid[0])
    result = 0
    
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 'G':
                plus_builder(grid, m, n, all_pluses, {(i, j)}, i, j, 1)
                
    all_pluses.sort(key=len, reverse=True)
    
    for i in range(0, len(all_pluses)):
        for j in range(i+1, len(all_pluses)):
            if all_pluses[i].isdisjoint(all_pluses[j]):
                result = max(result, len(all_pluses[i]) * len(all_pluses[j]))
                
    return result
    
    
def plus_builder(grid, m, n, pluses, subset, i, j, s):
    pluses.append(subset.copy())
    
    if i-s >= 0 and i+s < m and j-s >= 0 and j+s < n:
        if grid[i-s][j] == 'G' and grid[i+s][j] == 'G' and grid[i][j-s] == 'G' and grid[i][j+s] == 'G':
            subset.add((i-s, j))
            subset.add((i+s, j))
            subset.add((i, j-s))
            subset.add((i, j+s))
            plus_builder(grid, m, n, pluses, subset, i, j, s + 1)
    return    
    
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    grid = []

    for _ in range(n):
        grid_item = input()
        grid.append(grid_item)

    result = twoPluses(grid)

    fptr.write(str(result) + '\n')

    fptr.close()
