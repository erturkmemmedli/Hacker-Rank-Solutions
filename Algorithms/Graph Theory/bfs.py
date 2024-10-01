# Breadth First Search: Shortest Reach


#!/bin/python3

import math
import os
import random
import re
import sys

from heapq import heappush, heappop

#
# Complete the 'bfs' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
#  3. 2D_INTEGER_ARRAY edges
#  4. INTEGER s
#

def bfs(n, m, edges, s):
    # Write your code here
    graph = {i: set() for i in range(n)}
    
    for a, b in edges:
        graph[a - 1].add(b - 1)
        graph[b - 1].add(a - 1)
    
    distance = [math.inf] * n
    distance[s - 1] = 0
    heap = [(0, s - 1)]
    
    while heap:
        dist, node = heappop(heap)
        
        for neighbor in graph[node]:
            if distance[neighbor] > dist + 6:
                distance[neighbor] = dist + 6
                heappush(heap, (dist + 6, neighbor))
            
    distance.pop(s - 1)
    distance = [i if i != math.inf else -1 for i in distance]
    return distance
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        edges = []

        for _ in range(m):
            edges.append(list(map(int, input().rstrip().split())))

        s = int(input().strip())

        result = bfs(n, m, edges, s)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
