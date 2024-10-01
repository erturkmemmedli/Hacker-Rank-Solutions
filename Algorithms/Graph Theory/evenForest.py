# Even Tree


#!/bin/python3

import math
import os
import random
import re
import sys

from collections import deque

# Complete the evenForest function below.
def evenForest(t_nodes, t_edges, t_from, t_to):
    if t_nodes % 2 == 1:
        return 0
    
    graph = {i: [] for i in range(1, t_nodes + 1)}
    indegree = {i: [0, 1] for i in range(1, t_nodes + 1)}
    
    for a, b in zip(t_from, t_to):
        graph[a].append(b)
        graph[b].append(a)
        indegree[a][0] += 1
        indegree[b][0] += 1
        
    queue = deque([node for node in indegree.keys() if indegree[node][0] == 1])
    cut = -1
    
    while queue:
        node = queue.popleft()
        indegree[node][0] -= 1
        
        if indegree[node][1] % 2 == 0:
            cut += 1
        
        for neighbor in graph[node]:
            indegree[neighbor][0] -= 1
            indegree[neighbor][1] += indegree[node][1]
            
            if indegree[neighbor][0] == 1:
                queue.append(neighbor)
    
    return cut
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t_nodes, t_edges = map(int, input().rstrip().split())

    t_from = [0] * t_edges
    t_to = [0] * t_edges

    for i in range(t_edges):
        t_from[i], t_to[i] = map(int, input().rstrip().split())

    res = evenForest(t_nodes, t_edges, t_from, t_to)

    fptr.write(str(res) + '\n')

    fptr.close()
