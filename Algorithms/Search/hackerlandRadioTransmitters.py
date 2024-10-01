# Hackerland Radio Transmitters


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'hackerlandRadioTransmitters' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY x
#  2. INTEGER k
#

def hackerlandRadioTransmitters(x, k):
    # Write your code here
    x.sort()
    count = 0
    uncovered = 0
    transmitter = -1
    
    for i in range(1, len(x)):
        if x[i] - x[uncovered] > k and transmitter == -1:
            transmitter = i - 1
            count += 1
        if transmitter != -1 and x[i] - x[transmitter] > k:
            uncovered = i
            transmitter = -1
        print(uncovered, transmitter)
            
    if transmitter == -1:
        count += 1
        
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    x = list(map(int, input().rstrip().split()))

    result = hackerlandRadioTransmitters(x, k)

    fptr.write(str(result) + '\n')

    fptr.close()
