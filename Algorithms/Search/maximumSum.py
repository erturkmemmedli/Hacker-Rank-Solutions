# Maximum Subarray Sum


#!/bin/python3

import math
import os
import random
import re
import sys

from bisect import bisect_right, insort

#
# Complete the 'maximumSum' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. LONG_INTEGER_ARRAY a
#  2. LONG_INTEGER m
#

def maximumSum(a, m):
    # Write your code here
    maximum = 0
    current = 0
    prefix = []
    
    for num in a:
        current = (current + num) % m
        maximum = max(maximum, current)
        
        idx = bisect_right(prefix, current)
        
        if idx < len(prefix):
            maximum = max(maximum, current - prefix[idx] + m)
        
        insort(prefix, current)
        
        # low, high = 0, len(prefix)
        # while low < high:
        #     mid = (low + high) // 2
        #     if prefix[mid] > current:
        #         high = mid
        #     else:
        #         low = mid + 1
                
        # if low < len(prefix):
        #     maximum = max(maximum, current - prefix[low] + m)
        
        # prefix.insert(low, current)
    
    return maximum
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        a = list(map(int, input().rstrip().split()))

        result = maximumSum(a, m)

        fptr.write(str(result) + '\n')

    fptr.close()
