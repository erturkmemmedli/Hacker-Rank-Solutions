# Beautiful Triplets


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'beautifulTriplets' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER d
#  2. INTEGER_ARRAY arr
#

from collections import Counter

def beautifulTriplets(d, arr):
    # Write your code here
    counter = Counter(arr)
    triplets = 0
    
    for k, v in counter.items():
        if k - d in counter and k + d in counter:
            triplets += v * counter[k - d] * counter[k + d]
        
    return triplets
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    d = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    result = beautifulTriplets(d, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
