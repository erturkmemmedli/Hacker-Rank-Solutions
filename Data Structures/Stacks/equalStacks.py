# Equal Stacks


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'equalStacks' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY h1
#  2. INTEGER_ARRAY h2
#  3. INTEGER_ARRAY h3
#

def equalStacks(h1, h2, h3):
    # Write your code here
    i = j = k = 0
    a, b, c = sum(h1), sum(h2), sum(h3)
    
    while not (a == b == c) and a != 0 and b != 0 and c != 0:
        if a >= b and a >= c:
            a -= h1[i]
            i += 1
        elif b >= a and b >= c:
            b -= h2[j]
            j += 1
        elif c >= a and c >= b:
            c -= h3[k]
            k += 1
        
    return a

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n1 = int(first_multiple_input[0])

    n2 = int(first_multiple_input[1])

    n3 = int(first_multiple_input[2])

    h1 = list(map(int, input().rstrip().split()))

    h2 = list(map(int, input().rstrip().split()))

    h3 = list(map(int, input().rstrip().split()))

    result = equalStacks(h1, h2, h3)

    fptr.write(str(result) + '\n')

    fptr.close()
