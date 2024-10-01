# The Story of a Tree


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'storyOfATree' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY edges
#  3. INTEGER k
#  4. 2D_INTEGER_ARRAY guesses
#


def storyOfATree(n, edges, k, guesses):
    # Write your code here
    guesses = {tuple(g) for g in guesses}
    tree = {}
    
    for u, v in edges:
        tree.setdefault(u, []).append(v)
        tree.setdefault(v, []).append(u)
        
    cost = calculate_cost(tree, guesses)
    success = calculate_success(tree, guesses, cost, k)
    g = math.gcd(success, n)
    
    return "0/1" if success == 0 else f"{success//g}/{n//g}"
    
    
def calculate_cost(tree, guesses):
    root = 1
    visited = {root}
    stack = [root]
    count = 0
    
    while stack:
        root = stack.pop()
        
        for node in tree[root]:
            if node not in visited:
                visited.add(node)
                count += ((root, node) in guesses)
                stack.append(node)
                
    return count
    
    
def calculate_success(tree, guesses, cost, k):
    root = 1
    visited = {root}
    stack = [(root, cost)]
    success = 0
    
    while stack:
        root, cost = stack.pop()
        success += (cost >= k)
        
        for node in tree[root]:
            if node not in visited:
                visited.add(node)
                new_cost = cost - ((root, node) in guesses) + ((node, root) in guesses)
                stack.append((node, new_cost))
                
    return success
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        edges = []

        for _ in range(n - 1):
            edges.append(list(map(int, input().rstrip().split())))

        first_multiple_input = input().rstrip().split()

        g = int(first_multiple_input[0])

        k = int(first_multiple_input[1])

        guesses = []

        for _ in range(g):
            guesses.append(list(map(int, input().rstrip().split())))

        result = storyOfATree(n, edges, k, guesses)

        fptr.write(result + '\n')

    fptr.close()
