# Poisonous Plants


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'poisonousPlants' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY p as parameter.
#

from collections import deque

def poisonousPlants(p):
    # Write your code here
    stack = []
    
    for val in p:
        if not stack or stack[-1][-1] < val:
            stack.append(deque([val]))
        else:
            stack[-1].append(val)

    day = 0
    while len(stack) > 1:
        new_stack = [stack[0]]
        i = 1
        while i < len(stack):
            stack[i].popleft()
            if stack[i] and new_stack[-1][-1] >= stack[i][0]:
                new_stack[-1].extend(stack[i])
            elif stack[i]:
                new_stack.append(stack[i])
            i += 1
        
        stack = new_stack
        day += 1
        
    return day
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    p = list(map(int, input().rstrip().split()))

    result = poisonousPlants(p)

    fptr.write(str(result) + '\n')

    fptr.close()
