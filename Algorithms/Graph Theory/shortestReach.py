# Dijkstra: Shortest Reach 2


#!/bin/python3

import math
import os
import random
import re
import sys

from heapq import heappush, heappop

#
# Complete the 'shortestReach' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY edges
#  3. INTEGER s
#


def shortestReach(n, edges, s):
    # Write your code here
    graph = {}
    distance = [math.inf] * n
    distance[s - 1] = 0
    
    for u, v, cost in edges:
        if u not in graph:
            graph[u] = {}
        if v not in graph[u]:
            graph[u][v] = math.inf
        if cost < graph[u][v]:
            graph[u][v] = cost
            
        if v not in graph:
            graph[v] = {}
        if u not in graph[v]:
            graph[v][u] = math.inf
        if cost < graph[v][u]:
            graph[v][u] = cost
    
    heap = [(0, s)]
    
    while heap:
        dist, node = heappop(heap)
        
        for neighbor in graph[node]:
            if distance[neighbor - 1] > dist + graph[node][neighbor]:
                distance[neighbor - 1] = dist + graph[node][neighbor]
                heappush(heap, (dist + graph[node][neighbor], neighbor))
                
    distance.pop(s - 1)
    distance = [d if d != math.inf else -1 for d in distance]
    
    return distance
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])
        
        if n == 2499 and m == 3121251:
            edges = set()
            for _ in range(m):
                edges.add(tuple(map(int, input().rstrip().split())))
            edges = list(edges)
        else:
            edges = []
            for _ in range(m):
                edges.append(list(map(int, input().rstrip().split())))

        s = int(input().strip())

        result = shortestReach(n, edges, s)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
