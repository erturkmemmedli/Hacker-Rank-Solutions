# Game of Two Stacks


#!/bin/python3

import math
import os
import random
import re
import sys

from bisect import bisect_right

#
# Complete the 'twoStacks' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER maxSum
#  2. INTEGER_ARRAY a
#  3. INTEGER_ARRAY b
#

def twoStacks(maxSum, a, b):
    # Write your code here
    total = 0
    a_count = 0
     
    for i in range(len(a)):
        if a[i] + total <= maxSum:
            total += a[i]
            a_count += 1
        else:
            break
        
    b_count = 0
    overall = a_count
    
    for j in range(len(b)):
        while a_count > 0 and total + b[j] > maxSum:
            total -= a[a_count - 1]
            a_count -= 1
        
        if total + b[j] <= maxSum:
            total += b[j]
            b_count += 1
            overall = max(overall, a_count + b_count)
        else:
            break
            
    return overall
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    g = int(input().strip())

    for g_itr in range(g):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        maxSum = int(first_multiple_input[2])

        a = list(map(int, input().rstrip().split()))

        b = list(map(int, input().rstrip().split()))

        result = twoStacks(maxSum, a, b)

        fptr.write(str(result) + '\n')

    fptr.close()
