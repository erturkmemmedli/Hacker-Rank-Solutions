# Components in a graph


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'componentsInGraph' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts 2D_INTEGER_ARRAY gb as parameter.
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
            return
        
        if self.rank[ra] > self.rank[rb]:
            self.parent[rb] = ra
        elif self.rank[ra] == self.rank[rb]:
            self.parent[rb] = ra
            self.rank[ra] += 1
        else:
            self.parent[ra] = rb
            

def componentsInGraph(gb):
    # Write your code here
    n = len(gb)
    uf = UnionFind(n * 2)
    
    for a, b in gb:
        uf.union(a - 1, b - 1)
    
    parents = {}
    for i in range(n * 2):
        p = uf.find(i)
        parents[p] = parents.get(p, 0) + 1
    
    minimum = math.inf
    maximum = -math.inf
    
    for k, v in parents.items():
        if v != 1 and v < minimum:
            minimum = v
        if v != 1 and v > maximum:
            maximum = v
        
    return [minimum, maximum]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    gb = []

    for _ in range(n):
        gb.append(list(map(int, input().rstrip().split())))

    result = componentsInGraph(gb)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
