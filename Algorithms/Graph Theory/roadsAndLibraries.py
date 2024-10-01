# Roads and Libraries


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'roadsAndLibraries' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER c_lib
#  3. INTEGER c_road
#  4. 2D_INTEGER_ARRAY cities
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
            if self.rank[ra] > self.rank[rb]:
                self.parent[rb] = ra
            elif self.rank[ra] < self.rank[rb]:
                self.parent[ra] = rb
            else:
                self.parent[rb] = ra
                self.rank[ra] += 1
    

def roadsAndLibraries(n, c_lib, c_road, cities):
    # Write your code here
    uf = UnionFind(n)
    
    for a, b in cities:
        uf.union(a - 1, b - 1)
    
    city_map = {}
    
    for i in range(n):
        parent = uf.find(i - 1)
        city_map[parent] = city_map.get(parent, 0) + 1
    
    cost = 0
    
    for _, num_of_cities in city_map.items():
        num_of_edges = num_of_cities - 1
        
        if num_of_edges == 0:
            cost += c_lib
        elif c_lib >= c_road:
            cost += c_road * num_of_edges + c_lib
        else:
            cost += c_lib * num_of_cities
    
    return cost    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        c_lib = int(first_multiple_input[2])

        c_road = int(first_multiple_input[3])

        cities = []

        for _ in range(m):
            cities.append(list(map(int, input().rstrip().split())))

        result = roadsAndLibraries(n, c_lib, c_road, cities)

        fptr.write(str(result) + '\n')

    fptr.close()
