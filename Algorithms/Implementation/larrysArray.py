# Larry's Array


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'larrysArray' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER_ARRAY A as parameter.
#

def larrysArray(A):
    # Write your code here
    num = 0
    
    while num < len(A) - 2:
        idx = A.index(num + 1)

        if idx > num:
            i = num + (idx - num) % 2
            A.pop(idx)
            A.insert(i, num + 1)
            
            if i != num:
                A[i - 1], A[i], A[i + 1] = A[i], A[i + 1], A[i - 1]
            
        num += 1
    
    return "YES" if A[-1] > A[-2] else "NO"
       

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        A = list(map(int, input().rstrip().split()))

        result = larrysArray(A)

        fptr.write(result + '\n')

    fptr.close()
