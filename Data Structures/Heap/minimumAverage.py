# Minimum Average Waiting Time


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumAverage' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY customers as parameter.
#

from heapq import heappush, heappop


def minimumAverage(customers):
    # Write your code here
    customers.sort()
    total_time = customers[0][1] + customers[0][0]
    total_wait_time = customers[0][1]
    heap = []
    
    for i in range(1, len(customers)):
        time_come, time_wait = customers[i]
        
        while heap and time_come >= total_time:
            tw, tc = heappop(heap)
            total_time += tw
            total_wait_time += total_time - tc
            
        heappush(heap, (time_wait, time_come))
        
    while heap:
        tw, tc = heappop(heap)
        total_time += tw
        total_wait_time += total_time - tc
        
    return total_wait_time // len(customers)
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    customers = []

    for _ in range(n):
        customers.append(list(map(int, input().rstrip().split())))

    result = minimumAverage(customers)

    fptr.write(str(result) + '\n')

    fptr.close()
