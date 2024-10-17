# Flatland Space Stations


#!/bin/python3

import math
import os
import random
import re
import sys

from bisect import bisect_left

# Complete the flatlandSpaceStations function below.
def flatlandSpaceStations(n, c):
    c.sort()
    result = 0
    
    for i in range(n):
        idx = bisect_left(c, i)

        if idx == len(c):
            result = max(result, i - c[-1])
        elif idx == 0:
            result = max(result, c[0] - i)
        else:
            result = max(result, min(c[idx] - i, i - c[idx - 1]))
            
    return result
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    c = list(map(int, input().rstrip().split()))

    result = flatlandSpaceStations(n, c)

    fptr.write(str(result) + '\n')

    fptr.close()
