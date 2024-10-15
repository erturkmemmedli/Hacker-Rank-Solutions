# Minimum Distances


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumDistances' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def minimumDistances(a):
    # Write your code here
    min_pair = float('inf')
    hashmap = {}
    
    for i, num in enumerate(a):
        if num not in hashmap:
            hashmap[num] = []
            
        hashmap[num].append(i)
        
        if len(hashmap[num]) > 1:
            min_pair = min(min_pair, hashmap[num][-1] - hashmap[num][-2])
        
    return min_pair if min_pair != float('inf') else -1
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = minimumDistances(a)

    fptr.write(str(result) + '\n')

    fptr.close()
