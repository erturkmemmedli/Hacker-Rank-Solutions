# Prim's (MST) : Special Subtree


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'prims' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY edges
#  3. INTEGER start
#

from heapq import heappop, heappush


def prims(n, edges, start):
    # Write your code here
    graph = {}
    
    for u, v, c in edges:
        graph.setdefault(u, []).append((v, c))
        graph.setdefault(v, []).append((u, c))
        
    heap = [(0, start)]
    visited = set()
    total_cost = 0
    
    while heap:
        cost, node = heappop(heap)
                
        if node in visited:
            continue
        
        visited.add(node)
        total_cost += cost
        
        if len(visited) == n:
            return total_cost
        
        for neighbor, weight in graph[node]:
            heappush(heap, (weight, neighbor))
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    edges = []

    for _ in range(m):
        edges.append(list(map(int, input().rstrip().split())))

    start = int(input().strip())

    result = prims(n, edges, start)

    fptr.write(str(result) + '\n')

    fptr.close()
