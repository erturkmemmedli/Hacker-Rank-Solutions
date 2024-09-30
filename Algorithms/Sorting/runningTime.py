# Running Time of Algorithms


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'runningTime' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def runningTime(arr):
    # Write your code here
    counter = 0
    
    for i in range(1, n):
        if arr[i] >= arr[i - 1]:
            continue
        
        num = arr[i]
        j = i
        
        while j > 0 and arr[j - 1] > num:
            arr[j] = arr[j - 1]
            j -= 1
            counter += 1
            
        arr[j] = num
    
    return counter

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = runningTime(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
