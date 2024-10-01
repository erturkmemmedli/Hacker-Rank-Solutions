# Journey to the Moon


#!/bin/python3

import math
import os
import random
import re
import sys

from collections import Counter

#
# Complete the 'journeyToMoon' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY astronaut
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
        
        if ra != rb:
            if self.rank[rb] < self.rank[ra]:
                self.parent[rb] = ra
            elif self.rank[rb] > self.rank[ra]:
                self.parent[ra] = rb
            else:
                self.parent[rb] = ra
                self.rank[ra] += 1
                
    
def journeyToMoon(n, astronaut):
    # Write your code here
    uf = UnionFind(n)
    
    for a, b in astronaut:
        uf.union(a, b)
        
    hashmap = {}
    
    for i in range(n):
        root = uf.find(i)
        hashmap[root] = hashmap.get(root, 0) + 1
        
    counts = [(key, val) for key, val in Counter(hashmap.values()).items()]
    result = 0
        
    for i in range(len(counts)):
        x, y = counts[i]
        for j in range(i, len(counts)):
            z, t = counts[j]
            if i == j:
                result += math.comb(x, 1) ** 2 * y * (y - 1) // 2
            else:
                result += math.comb(x, 1) * math.comb(z, 1) * y * t
                
    return result
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    p = int(first_multiple_input[1])

    astronaut = []

    for _ in range(p):
        astronaut.append(list(map(int, input().rstrip().split())))

    result = journeyToMoon(n, astronaut)

    fptr.write(str(result) + '\n')

    fptr.close()
