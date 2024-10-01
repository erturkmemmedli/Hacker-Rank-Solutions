# Construct the Array


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countArray' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. INTEGER x
#

def countArray(n, k, x):
    # Return the number of ways to fill in the array.
    mod = 1_000_000_007
    
    prev_x = int(x == 1)
    prev_not_x = int(not prev_x)
            
    for i in range(2, n):
        tmp = prev_not_x
        prev_not_x = (prev_x * (k-1) + prev_not_x * (k-2)) % mod
        prev_x = tmp
        
    return prev_not_x


def countArray_alternative(n, k, x):
    # Return the number of ways to fill in the array.
    mod = 1_000_000_007
    
    dp = [[None for _ in range(n)] for _ in range(2)]
            
    dp[0][0] = 1 if x == 1 else 0
    dp[1][0] = 0 if x == 1 else 1

    for i in range(1, n):
        dp[0][i] = dp[1][i - 1] % mod
        dp[1][i] = (dp[0][i - 1] * (k - 1) + dp[1][i - 1] * (k - 2)) % mod

    return dp[0][n - 1]
    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    x = int(first_multiple_input[2])

    answer = countArray(n, k, x)

    fptr.write(str(answer) + '\n')

    fptr.close()
