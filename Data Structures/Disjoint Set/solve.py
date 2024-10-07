# Super Maximum Cost Queries


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'solve' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. 2D_INTEGER_ARRAY tree
#  2. 2D_INTEGER_ARRAY queries
#

from bisect import bisect_right


class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.size = [1] * n
        
    def find(self, a):
        while a != self.parent[a]:
            a = self.parent[a]
        return a
        
    def union(self, a, b, cost_map, cost):
        ra = self.find(a)
        rb = self.find(b)
        cost_map[cost] += self.size[ra] * self.size[rb]
        
        if ra == rb:
            return
        
        if self.rank[ra] < self.rank[rb]:
            self.parent[ra] = rb
            self.size[rb] += self.size[ra]
        elif self.rank[rb] < self.rank[ra]:
            self.parent[rb] = ra
            self.size[ra] += self.size[rb]
        else:
            self.rank[ra] += 1
            self.parent[rb] = ra
            self.size[ra] += self.size[rb]
            

def solve(tree, queries):
    # Write your code here
    n = len(tree) + 1
    
    uf = UnionFind(n)
    cost_map = {0: 0}
    costs_sorted = [0]
    prev_cost = 0
    result = []
    
    tree.sort(key=lambda x: x[2])
    
    for u, v, cost in tree:
        if cost != prev_cost:
            costs_sorted.append(cost)
            cost_map[cost] = cost_map[prev_cost]
        
        uf.union(u - 1, v - 1, cost_map, cost)
        prev_cost = cost

    for x, y in queries:
        i = bisect_right(costs_sorted, x - 1)
        cost_x = costs_sorted[i - 1]
        j = bisect_right(costs_sorted, y)
        cost_y = costs_sorted[j - 1]
        result.append(cost_map[cost_y] - cost_map[cost_x])
        
    return result
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    q = int(first_multiple_input[1])

    tree = []

    for _ in range(n - 1):
        tree.append(list(map(int, input().rstrip().split())))

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    result = solve(tree, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
