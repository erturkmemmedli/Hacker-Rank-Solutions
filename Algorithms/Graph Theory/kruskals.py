# Kruskal (MST): Really Special Subtree


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'kruskals' function below.
#
# The function is expected to return an INTEGER.
# The function accepts WEIGHTED_INTEGER_GRAPH g as parameter.
#

#
# For the weighted graph, <name>:
#
# 1. The number of nodes is <name>_nodes.
# 2. The number of edges is <name>_edges.
# 3. An edge exists between <name>_from[i] and <name>_to[i]. The weight of the edge is <name>_weight[i].
#
#

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
        
    def find(self, a):
        while a != self.parent[a]:
            a = self.parent[a]
        return a
        
    def union(self, a, b):
        ra = self.find(a)
        rb = self.find(b)
        
        if ra == rb:
            return False
            
        if self.rank[ra] > self.rank[rb]:
            self.parent[rb] = ra
        elif self.rank[ra] < self.rank[rb]:
            self.parent[ra] = rb
        else:
            self.rank[ra] += 1
            self.parent[rb] = ra
        
        return True
        

def kruskals(g_nodes, g_from, g_to, g_weight):
    # Write your code here
    edges = [(z, x, y) for x, y, z in zip(g_from, g_to, g_weight)]
    edges.sort()
    
    uf = UnionFind(g_nodes)
    total = 0
    
    for weight, a, b in edges:
        if uf.union(a - 1, b - 1):
            total += weight
            
    return total
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    g_nodes, g_edges = map(int, input().rstrip().split())

    g_from = [0] * g_edges
    g_to = [0] * g_edges
    g_weight = [0] * g_edges

    for i in range(g_edges):
        g_from[i], g_to[i], g_weight[i] = map(int, input().rstrip().split())

    res = kruskals(g_nodes, g_from, g_to, g_weight)

    # Write your code here.
    fptr.write(str(res))

    fptr.close()
