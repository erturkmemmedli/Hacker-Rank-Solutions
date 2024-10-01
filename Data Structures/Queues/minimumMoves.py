# Castle on the Grid


#!/bin/python3

import math
import os
import random
import re
import sys

from heapq import heappush, heappop

#
# Complete the 'minimumMoves' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING_ARRAY grid
#  2. INTEGER startX
#  3. INTEGER startY
#  4. INTEGER goalX
#  5. INTEGER goalY
#

def minimumMoves(grid, startX, startY, goalX, goalY):
    # Write your code here
    n = len(grid)
    heap = [(0, startX, startY, None)]
    visited = set()
    
    while heap:
        step, r, c, d = heappop(heap)
        if r == goalX and c == goalY:
            return step
        if 0 <= r-1 < n > c >= 0 and grid[r-1][c] == '.' and (r-1, c, 'up') not in visited:
            heappush(heap, (step + 1 if d != 'up' else step, r-1, c, 'up'))
            visited.add((r-1, c, 'up'))
        if 0 <= r+1 < n > c >= 0 and grid[r+1][c] == '.' and (r+1, c, 'down') not in visited:
            heappush(heap, (step + 1 if d != 'down' else step, r+1, c, 'down'))
            visited.add((r+1, c, 'down'))
        if 0 <= r < n > c-1 >= 0 and grid[r][c-1] == '.' and (r, c-1, 'left') not in visited:
            heappush(heap, (step + 1 if d != 'left' else step, r, c-1, 'left'))
            visited.add((r, c-1, 'left'))
        if 0 <= r < n > c+1 >= 0 and grid[r][c+1] == '.' and (r, c+1, 'right') not in visited:
            heappush(heap, (step + 1 if d != 'right' else step, r, c+1, 'right'))
            visited.add((r, c+1, 'right'))
                                
    return -1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    grid = []

    for _ in range(n):
        grid_item = input()
        grid.append(grid_item)

    first_multiple_input = input().rstrip().split()

    startX = int(first_multiple_input[0])

    startY = int(first_multiple_input[1])

    goalX = int(first_multiple_input[2])

    goalY = int(first_multiple_input[3])

    result = minimumMoves(grid, startX, startY, goalX, goalY)

    fptr.write(str(result) + '\n')

    fptr.close()
