# Connected Cells in a Grid


#!/bin/python3

import math
import os
import random
import re
import sys

from collections import deque

#
# Complete the 'connectedCell' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY matrix as parameter.
#

def connectedCell(matrix):
    # Write your code here
    m, n = len(matrix), len(matrix[0])
    visited = set()
    max_area = 0
    
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 1:
                queue = deque([(i, j)])
                visited.add((i, j))
                area = 0
                
                while queue:
                    r, c = queue.popleft()
                    area += 1
                    
                    for row, col in (r-1,c-1), (r-1,c), (r+1,c), (r,c-1), (r,c+1), (r+1,c-1), (r+1,c), (r+1, c+1):
                        if 0 <= row < m and 0 <= col < n and (row, col) not in visited and matrix[row][col] == 1:
                            visited.add((row, col))
                            queue.append((row, col))
                max_area = max(max_area, area)
                
    return max_area
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    m = int(input().strip())

    matrix = []

    for _ in range(n):
        matrix.append(list(map(int, input().rstrip().split())))

    result = connectedCell(matrix)

    fptr.write(str(result) + '\n')

    fptr.close()
