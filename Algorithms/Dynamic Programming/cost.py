# Sherlock and Cost


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'cost' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY B as parameter.
#

def cost(B):
    # Write your code here
    A = [[0], [0]]
    
    for i in range(1, len(B)):
        x = max(abs(B[i] - B[i - 1]) + A[0][-1], abs(B[i] - 1) + A[1][-1])
        y = abs(1 - B[i - 1]) + A[0][-1]
        A[0].append(x)
        A[1].append(y)

    return max(A[0][-1], A[1][-1])

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        B = list(map(int, input().rstrip().split()))

        result = cost(B)

        fptr.write(str(result) + '\n')

    fptr.close()
