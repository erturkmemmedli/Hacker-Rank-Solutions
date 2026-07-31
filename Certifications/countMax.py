#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the 'countMax' function below.
# The function is expected to return a LONG_INTEGER.
# The function accepts STRING_ARRAY upRight as parameter.

def countMax(upRight):
    # Write your code here
    min_r = min_c = float('inf')
    for s in upRight:
        r, c = s.split()
        min_r = min(min_r, int(r))
        min_c = min(min_c, int(c))
    return min_r * min_c

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    upRight_count = int(input().strip())

    upRight = []

    for _ in range(upRight_count):
        upRight_item = input()
        upRight.append(upRight_item)

    result = countMax(upRight)

    fptr.write(str(result) + '\n')

    fptr.close()
