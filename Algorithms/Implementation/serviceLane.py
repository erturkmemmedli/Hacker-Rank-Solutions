# Service Lane


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'serviceLane' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY cases
#

class SegmentTreeNode:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.total = float('inf')
        self.left = None
        self.right = None
        

class SegmentTree:
    def __init__(self, nums):
        def createTree(nums, l, r):
            if l > r:
                return None
                
            if l == r:
                n = SegmentTreeNode(l, r)
                n.total = nums[l]
                return n
            
            mid = (l + r) // 2
            root = SegmentTreeNode(l, r)
            root.left = createTree(nums, l, mid)
            root.right = createTree(nums, mid + 1, r)
            root.total = min(root.left.total, root.right.total)
            return root
        
        self.root = createTree(nums, 0, len(nums) - 1)

    def update(self, index, val):
        def updateVal(root, i, val):
            if root.start == root.end:
                root.total = val
                return val
        
            mid = (root.start + root.end) // 2
            
            if i <= mid:
                updateVal(root.left, i, val)
            else:
                updateVal(root.right, i, val)
            
            root.total = min(root.left.total, root.right.total)
            return root.total
        
        return updateVal(self.root, index, val)

    def minRange(self, left, right):
        def rangeMin(root, i, j):
            if root.start == i and root.end == j:
                return root.total
            
            mid = (root.start + root.end) // 2

            if j <= mid:
                return rangeMin(root.left, i, j)
            elif i >= mid + 1:
                return rangeMin(root.right, i, j)
            else:
                return min(rangeMin(root.left, i, mid), rangeMin(root.right, mid + 1, j))
        
        return rangeMin(self.root, left, right)


def serviceLane(n, cases, width):
    # Write your code here
    tree = SegmentTree(width)
    answer = []
        
    for l, r in cases:
        answer.append(tree.minRange(l, r))
        
    return answer
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    t = int(first_multiple_input[1])

    width = list(map(int, input().rstrip().split()))

    cases = []

    for _ in range(t):
        cases.append(list(map(int, input().rstrip().split())))

    result = serviceLane(n, cases, width)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
