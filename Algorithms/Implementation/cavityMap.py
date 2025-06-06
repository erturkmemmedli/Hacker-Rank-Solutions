# Cavity Map


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'cavityMap' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts STRING_ARRAY grid as parameter.
#

def cavityMap(grid):
    # Write your code here
    n = len(grid)
    
    for i in range(1, n-1):
        for j in range(1, n-1):
            for r, c in [i-1, j], [i+1, j], [i, j-1], [i, j+1]:
                if grid[r][c] == 'X' or int(grid[i][j]) <= int(grid[r][c]):
                    break
            else:
                grid[i] = grid[i][:j] + 'X' + grid[i][j+1:]
    
    return grid

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    grid = []

    for _ in range(n):
        grid_item = input()
        grid.append(grid_item)

    result = cavityMap(grid)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
