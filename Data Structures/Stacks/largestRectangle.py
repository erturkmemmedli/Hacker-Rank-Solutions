# Largest Rectangle


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'largestRectangle' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts INTEGER_ARRAY h as parameter.
#

def largestRectangle(h):
    # Write your code here
    stack = []
    max_area = 0
    
    for height in h:
        while stack and stack[-1][0] >= height:
            if len(stack) > 1 and stack[-2][0] > height:
                stack[-2][1] += stack.pop()[1]
                max_area = max(max_area, stack[-1][0] * stack[-1][1])
            else:
                stack[-1][0] = height
                stack[-1][1] += 1
                max_area = max(max_area, stack[-1][0] * stack[-1][1])
                break
                
        if not stack or stack[-1][0] < height:
            stack.append([height, 1])
            max_area = max(max_area, height)

    while stack:
        h, w = stack.pop()
        max_area = max(max_area, h * w)
        if stack:
            stack[-1][1] += w
        
    return max_area

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    h = list(map(int, input().rstrip().split()))

    result = largestRectangle(h)

    fptr.write(str(result) + '\n')

    fptr.close()
