# Find Maximum Index Product


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'solve' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

from collections import deque

def solve(arr):
    # Write your code here
    n = len(arr)
    left_stack = [(arr[0], 1)]
    right_stack = [(arr[n - 1], n)]
    left = deque([0])
    right = deque([0])
    
    for i in range(1, n):
        while left_stack and arr[i] >= left_stack[-1][0]:
            left_stack.pop()
        left.append(left_stack[-1][1] if left_stack else 0)
        left_stack.append((arr[i], i + 1))
        
    for i in range(n - 2, -1, -1):
        while right_stack and arr[i] >= right_stack[-1][0]:
            right_stack.pop()
        right.appendleft(right_stack[-1][1] if right_stack else 0)
        right_stack.append((arr[i], i + 1))
    
    return max(a * b for a, b in zip(left, right))
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = solve(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
