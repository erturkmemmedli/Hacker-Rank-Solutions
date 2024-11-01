# Truck Tour


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'truckTour' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY petrolpumps as parameter.
#

def truckTour(petrolpumps):
    # Write your code here
    petrolpumps = [a - b for a, b in petrolpumps]
    start_index = None
    amount = 0
    
    for i, num in enumerate(petrolpumps):
        if amount + num < 0:
            amount = 0
            start_index = None
            continue
    
        if not start_index:
            start_index = i
            
        amount += num
        
    return start_index

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    petrolpumps = []

    for _ in range(n):
        petrolpumps.append(list(map(int, input().rstrip().split())))

    result = truckTour(petrolpumps)

    fptr.write(str(result) + '\n')

    fptr.close()
