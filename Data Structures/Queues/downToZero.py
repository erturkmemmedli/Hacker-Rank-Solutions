# Down to Zero II


#!/bin/python3

import math
import os
import random
import re
import sys

from heapq import heappop, heappush

#
# Complete the 'downToZero' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def downToZero(n):
    # Write your code here
    heap = [(0, n)]
    visited = set()
    
    while heap:
        step, n = heappop(heap)
        
        if n == 0:
            return step
        
        if n - 1 not in visited:
            visited.add(n - 1)
            heappush(heap, (step + 1, n - 1))
        
        for num in range(int(math.sqrt(n)), 1, -1):
            if n % num == 0 and n // num not in visited:
                visited.add(n // num)
                heappush(heap, (step + 1, n // num))
                
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        result = downToZero(n)

        fptr.write(str(result) + '\n')

    fptr.close()
