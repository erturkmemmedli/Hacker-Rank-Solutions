# Problem Solving (Intermediate): 1. Equalizing Array Elements

#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'minOperations' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY arr
#  2. INTEGER threshold
#  3. INTEGER d
#

from collections import defaultdict

def minOperations(arr, threshold, d):
    # Write your code here
    costs = defaultdict(list)
    for x in arr:
        ops = 0
        while True:
            costs[x].append(ops)
            if x == 0:
                break
            x //= d
            ops += 1

    best = float('inf')
    for c in costs.values():
        if len(c) >= threshold:
            c.sort()
            best = min(best, sum(c[:threshold]))
    return best


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = []

    for _ in range(arr_count):
        arr_item = int(input().strip())
        arr.append(arr_item)

    threshold = int(input().strip())

    d = int(input().strip())

    result = minOperations(arr, threshold, d)

    fptr.write(str(result) + '\n')

    fptr.close()
