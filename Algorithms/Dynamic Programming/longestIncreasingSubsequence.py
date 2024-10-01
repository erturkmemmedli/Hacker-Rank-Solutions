# The Longest Increasing Subsequence


#!/bin/python3

import math
import os
import random
import re
import sys

from bisect import bisect_left

#
# Complete the 'longestIncreasingSubsequence' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def longestIncreasingSubsequence(arr):
    # Write your code here
    stack = []
    
    for num in arr:
        idx = bisect_left(stack, num)
        if idx == len(stack):
            stack.append(num)
        else:
            stack[idx] = num
    
    return len(stack)
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr_item = int(input().strip())
        arr.append(arr_item)

    result = longestIncreasingSubsequence(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
