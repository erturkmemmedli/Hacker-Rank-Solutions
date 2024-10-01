# Snakes and Ladders: The Quickest Way Up


#!/bin/python3

import math
import os
import random
import re
import sys

from collections import deque

#
# Complete the 'quickestWayUp' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. 2D_INTEGER_ARRAY ladders
#  2. 2D_INTEGER_ARRAY snakes
#

def quickestWayUp(ladders, snakes):
    # Write your code here
    position_map = {i: i for i in range(1, 101)}
    
    for src, dst in ladders:
        position_map[src] = dst
        
    for src, dst in snakes:
        position_map[src] = dst
        
    queue = deque([(1, 0)])
    visited = {1}
    
    while queue:
        position, distance = queue.popleft()
        
        if position == 100:
            return distance
        
        for dice in range(6, 0, -1):
            if position + dice <= 100 and position_map[position + dice] not in visited:
                visited.add(position_map[position + dice])
                queue.append((position_map[position + dice], distance + 1))
                
    return -1
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        ladders = []

        for _ in range(n):
            ladders.append(list(map(int, input().rstrip().split())))

        m = int(input().strip())

        snakes = []

        for _ in range(m):
            snakes.append(list(map(int, input().rstrip().split())))

        result = quickestWayUp(ladders, snakes)

        fptr.write(str(result) + '\n')

    fptr.close()
