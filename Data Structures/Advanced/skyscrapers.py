# Jim and the Skyscrapers


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'solve' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def solve(arr):
    # Write your code here
    stack = []
    count = 0
    
    for num in arr:
        while stack and num > stack[-1][0]:
            val, cnt = stack.pop()
            count += (cnt - 1) * cnt // 2
        
        if stack and stack[-1][0] == num:
            stack[-1][1] += 1
        else:
            stack.append([num, 1])
            
    while stack:
        val, cnt = stack.pop()
        count += (cnt - 1) * cnt // 2
        
    return count * 2
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = solve(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
