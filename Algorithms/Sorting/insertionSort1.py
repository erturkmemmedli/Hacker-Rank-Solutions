# Insertion Sort - Part 1


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    # Write your code here
    for i in range(1, n):
        if arr[i] >= arr[i - 1]:
            continue
           
        num = arr[i]
        j = i
        
        while j > 0 and arr[j - 1] > num:
            arr[j] = arr[j - 1]
            print(*arr, sep=" ")
            j -= 1
        
        arr[j] = num
        print(*arr, sep=" ")
        

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
