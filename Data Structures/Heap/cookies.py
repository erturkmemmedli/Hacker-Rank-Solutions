# Jesse and Cookies


#!/bin/python3

import math
import os
import random
import re
import sys

from heapq import heappush, heappop

#
# Complete the 'cookies' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY A
#

def cookies(k, A):
    # Write your code here
    heap = []
    for num in A:
        heappush(heap, num)
    
    count = 0
    while len(heap) > 1 and heap[0] < k:
        first = heappop(heap)
        second = heappop(heap)
        heappush(heap, first + 2 * second)
        count += 1
    
    return -1 if heap[0] < k else count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    A = list(map(int, input().rstrip().split()))

    result = cookies(k, A)

    fptr.write(str(result) + '\n')

    fptr.close()
