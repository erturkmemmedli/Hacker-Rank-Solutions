# Queries with Fixed Length


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
#  1. INTEGER_ARRAY arr
#  2. INTEGER_ARRAY queries
#

from collections import deque

def solve(arr, queries):
    # Write your code here
    result = []
    
    for q in queries:
        result.append(sliding_window_max(arr, q))
    
    return result
    
    
def sliding_window_max(arr, k):
    queue = deque()
    result = []
    
    for i, num in enumerate(arr):
        if queue and i - queue[0][1] == k:
            queue.popleft()
            
        while queue and queue[-1][0] < num:
            queue.pop()
            
        queue.append([num, i])
        
        if i >= k - 1:
            result.append(queue[0][0])
            
    return min(result)
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    q = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    queries = []

    for _ in range(q):
        queries_item = int(input().strip())
        queries.append(queries_item)

    result = solve(arr, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
