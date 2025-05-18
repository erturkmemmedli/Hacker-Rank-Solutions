# The Maximum Subarray

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'maxSubarray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def maxSubarray(arr):
    # Write your code here
    with_neg = max(arr)
    if with_neg <= 0:
        return with_neg, with_neg
    
    curr = only_pos = 0
    for num in arr:
        only_pos += max(0, num)
        curr = max(0, curr + num)
        with_neg = max(with_neg, curr)

    return with_neg, only_pos
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = maxSubarray(arr)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
