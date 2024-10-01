# Kingdom Division


#!/bin/python3

import math
import os
import random
import re
import sys

from collections import deque

#
# Complete the 'kingdomDivision' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY roads
#

sys.setrecursionlimit(100000)
MOD = 1_000_000_007


def kingdomDivision(n, roads):
    # Write your code here
    graph = {}
    degree = {}
    
    for u, v in roads:
        graph.setdefault(u, set()).add(v)
        graph.setdefault(v, set()).add(u)
        degree[u] = degree.get(u, 0) + 1
        degree[v] = degree.get(v, 0) + 1
        
    count = {i: {True: 1, False: 1} for i in degree}
    leaves = deque([i for i in degree if degree[i] == 1])
    
    while True:
        node = leaves.popleft()
        count[node][False] = count[node][True] - count[node][False]

        if not degree[node]:
            root = node
            break
        else:
            parent = graph[node].pop()
            graph[parent].discard(node)
            degree[parent] -= 1
            
            if degree[parent] == 1:
                leaves.append(parent)

            count[parent][True] *= count[node][True] + count[node][False]
            count[parent][False] *= count[node][False]

    total = 2 * count[root][0]
    return total % MOD
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    roads = []

    for _ in range(n - 1):
        roads.append(list(map(int, input().rstrip().split())))

    result = kingdomDivision(n, roads)

    fptr.write(str(result) + '\n')

    fptr.close()
