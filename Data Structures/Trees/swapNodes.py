# Swap Nodes [Algo]


#!/bin/python3

import math
import os
import random
import re
import sys

from collections import deque

sys.setrecursionlimit(10000)

#
# Complete the 'swapNodes' function below.
#
# The function is expected to return a 2D_INTEGER_ARRAY.
# The function accepts following parameters:
#  1. 2D_INTEGER_ARRAY indexes
#  2. INTEGER_ARRAY queries
#

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def inorder(res, root):
    if not root:
        return
    inorder(res, root.left)
    res.append(root.val)
    inorder(res, root.right)

def swapNodes(indexes, queries):
    # Write your code here
    result = []
    root = Node(1)
    queue = deque([root])
    
    for l, r in indexes:
        node = queue.popleft()
        if l != -1:
            left = Node(l)
            node.left = left
            queue.append(left)
        if r != -1:
            right = Node(r)
            node.right = right
            queue.append(right)
        
    for k in queries:
        queue = deque([root])
        level = 0
        while queue:
            length = len(queue)
            level += 1
            for _ in range(length):
                node = queue.popleft()
                if level % k == 0:
                    node.left, node.right = node.right, node.left
                    res = []
                    inorder(res, root)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        res = []
        inorder(res, root)
        result.append(res)
    
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    indexes = []

    for _ in range(n):
        indexes.append(list(map(int, input().rstrip().split())))

    queries_count = int(input().strip())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input().strip())
        queries.append(queries_item)

    result = swapNodes(indexes, queries)

    fptr.write('\n'.join([' '.join(map(str, x)) for x in result]))
    fptr.write('\n')

    fptr.close()
