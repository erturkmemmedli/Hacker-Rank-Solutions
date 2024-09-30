# Dynamic Array


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'dynamicArray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#

def dynamicArray(n, queries):
    # Write your code here
    last_answer = 0
    answers = []
    
    arr = [[] for _ in range(n)]
    for q, x, y in queries:
        if q == 1:
            idx = (x ^ last_answer) % n
            arr[idx].append(y)
        elif q == 2:
            idx = (x ^ last_answer) % n
            last_answer = arr[idx][y % len(arr[idx])]
            answers.append(last_answer)
        
    return answers
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    q = int(first_multiple_input[1])

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    result = dynamicArray(n, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
