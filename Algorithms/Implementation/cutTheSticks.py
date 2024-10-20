# Cut the sticks


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'cutTheSticks' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

from collections import Counter

def cutTheSticks(arr):
    # Write your code here
    n = len(arr)
    counter = sorted([(key, val) for key, val in Counter(arr).items()])
    result = []
    
    for k, v in counter:
        result.append(n)
        n -= v
    
    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = cutTheSticks(arr)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
