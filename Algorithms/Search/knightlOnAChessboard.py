# KnightL on a Chessboard


#!/bin/python3

import math
import os
import random
import re
import sys

from collections import deque

#
# Complete the 'knightlOnAChessboard' function below.
#
# The function is expected to return a 2D_INTEGER_ARRAY.
# The function accepts INTEGER n as parameter.
#
        
def bfs(i, j, n):
    queue = deque([(0, 0, 0)])
    visited = {(0, 0)}
    
    while queue:
        r, c, step = queue.popleft()
        
        if r == n - 1 and c == n - 1:
            return step
        
        for a, b in [i, j], [i, -j], [-i, j], [-i, -j], [j, i], [j, -i], [-j, i], [-j, -i]:
            if (r + a, c + b) not in visited and 0 <= r + a < n and 0 <= c + b < n:
                visited.add((r + a, c + b))
                queue.append((r + a, c + b, step + 1))
            
    return -1

def knightlOnAChessboard(n):
    # Write your code here
    matrix = [[None] * (n - 1) for _ in range(n - 1)]
    
    for i in range(1, n):
        for j in range(i, n):
            res = bfs(i, j, n)
            matrix[i - 1][j - 1] = res
            matrix[j - 1][i - 1] = res
    
    return matrix
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())
    result = knightlOnAChessboard(n)

    fptr.write('\n'.join([' '.join(map(str, x)) for x in result]))
    fptr.write('\n')

    fptr.close()
