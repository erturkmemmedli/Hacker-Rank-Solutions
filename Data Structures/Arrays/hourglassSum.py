#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'hourglassSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def hourglassSum(arr):
    # Write your code here
    hourglass = -float('inf')
    
    for i in range(1, len(arr) - 1):
        for j in range(1, len(arr) - 1):
            up = arr[i-1][j-1] + arr[i-1][j] + arr[i-1][j+1]
            down = arr[i+1][j-1] + arr[i+1][j] + arr[i+1][j+1]
            hourglass = max(hourglass, up + down + arr[i][j])
            
    return hourglass
            
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
