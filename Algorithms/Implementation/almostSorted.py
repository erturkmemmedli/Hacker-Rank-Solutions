# Almost Sorted


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'almostSorted' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def almostSorted(arr):
    # Write your code here
    sorted_arr = sorted([(num, i) for i, num in enumerate(arr)])
    indices = []
    first_instance = None
    
    for i in range(len(arr)):
        if arr[i] != sorted_arr[i][0]:
            indices.append(sorted_arr[i][1])
            if first_instance is None:
                first_instance = [i, sorted_arr[i][1]]
    
    if len(indices) == 0:
        print("yes")
    elif len(indices) == 2:
        print("yes")
        print("swap", first_instance[0] + 1, first_instance[1] + 1)
    elif indices[::-1] == sorted(indices):
        print("yes")
        print("reverse", indices[-1] + 1, indices[0] + 1)
    else:
        print("no")
        

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    almostSorted(arr)
