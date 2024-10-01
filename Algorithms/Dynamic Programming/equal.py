# Equal


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'equal' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def equal(arr):
    # Write your code here
    result = math.inf
    minimum = min(arr)
    
    for base in range(3):
        step = 0
        for num in arr:
            distance = num - (minimum - base)
            step += (distance // 5) + (distance % 5 // 2) + (distance % 5 % 2)
        result = min(result, step)
    
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = equal(arr)

        fptr.write(str(result) + '\n')

    fptr.close()
