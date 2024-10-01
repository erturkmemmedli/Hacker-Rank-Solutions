# Minimum Loss


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumLoss' function below.
#
# The function is expected to return an INTEGER.
# The function accepts LONG_INTEGER_ARRAY price as parameter.
#

def minimumLoss(price):
    # Write your code here
    sorted_price = sorted([(val, i) for i, val in enumerate(price)], reverse=True)
    min_price = math.inf
    
    for i in range(len(price) - 1):
        if sorted_price[i][1] < sorted_price[i + 1][1]:
            min_price = min(min_price, sorted_price[i][0] - sorted_price[i + 1][0])

    return min_price

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    price = list(map(int, input().rstrip().split()))

    result = minimumLoss(price)

    fptr.write(str(result) + '\n')

    fptr.close()
