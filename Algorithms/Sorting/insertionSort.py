# Insertion Sort Advanced Analysis


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

sys.setrecursionlimit(10000)


def insertionSort(arr):
    # Write your code here
    solution = NumberOfInversions()
    solution.mergeSort(arr)
    return solution.inversion

class NumberOfInversions:
    def __init__(self):
        self.inversion = 0
        
    def mergeSort(self, arr):
        if len(arr) == 1:
            return arr
            
        mid = len(arr) // 2
        
        first = self.mergeSort(arr[:mid])
        second = self.mergeSort(arr[mid:])
        
        res = self.merge(first, second)
        return res
        
    def merge(self, a, b):
        res = []
        i = j = 0
        
        while i < len(a) and j < len(b):
            if a[i] <= b[j]:
                res.append(a[i])
                i += 1
            else:
                res.append(b[j])
                j += 1
                self.inversion += len(a) - i
        
        res.extend(a[i:] if j == len(b) else b[j:])
        return res
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = insertionSort(arr)

        fptr.write(str(result) + '\n')

    fptr.close()
