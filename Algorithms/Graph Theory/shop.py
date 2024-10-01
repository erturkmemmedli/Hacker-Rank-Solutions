# Synchronous Shopping


#!/bin/python3

import math
import os
import random
import re
import sys

from heapq import heappop, heappush

#
# Complete the 'shop' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. STRING_ARRAY centers
#  4. 2D_INTEGER_ARRAY roads
#

def shop(n, k, centers, roads):
    # Write your code here
    bitmask = {i: 0 for i in range(n)}
    
    for i, center in enumerate(centers):
        for fish_type in list(map(int, center.rstrip().split()))[1:]:
            if fish_type > 0:
                bitmask[i] = bitmask[i] | 1 << (fish_type - 1)
            
    print(bitmask)
    graph = {}
    
    for city1, city2, cost in roads:
        graph.setdefault(city1 - 1, []).append((city2 - 1, cost))
        graph.setdefault(city2 - 1, []).append((city1 - 1, cost))
       
    distances = [[math.inf] * (2 ** k) for _ in range(n)]
    distances[0][bitmask[0]] = 0
    heap = [(0, 0, bitmask[0])]
    
    while heap:
        distance, curr_city, mask = heappop(heap)
        
        for neighbor_city, cost in graph[curr_city]:
            new_mask = mask | bitmask[neighbor_city]
            new_distance = distance + cost
            if distances[neighbor_city][new_mask] > new_distance:
                distances[neighbor_city][new_mask] = new_distance
                heappush(heap, (new_distance, neighbor_city, new_mask))
    
    result = math.inf
    
    for i in range(2 ** k):
        for j in range(i, 2 ** k):
            if distances[-1][i] != math.inf and distances[-1][j] != math.inf and i | j == (1 << k) - 1:
                result = min(result, max(distances[-1][i], distances[-1][j]))
    
    return result
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    k = int(first_multiple_input[2])

    centers = []

    for _ in range(n):
        centers_item = input()
        centers.append(centers_item)

    roads = []

    for _ in range(m):
        roads.append(list(map(int, input().rstrip().split())))

    res = shop(n, k, centers, roads)

    fptr.write(str(res) + '\n')

    fptr.close()
