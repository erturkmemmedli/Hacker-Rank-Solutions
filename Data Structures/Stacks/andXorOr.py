#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'andXorOr' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def andXorOr(a):
    # Write your code here
    stack = []
    res = 0
    
    '''
    Truth Table:
      a   b   a^b   a&b   a|b    (a&b)^(a|b)
    | 0 | 0 |  0  |  0  |  0  |       0      |
    | 0 | 1 |  1  |  0  |  1  |       1      |
    | 1 | 0 |  1  |  0  |  1  |       1      |
    | 1 | 1 |  0  |  1  |  1  |       0      |

    So, (a&b)^(a|b) = a^b
    '''
  
    for val in a:
        while stack:
            res = max(res, val ^ stack[-1])
            if val < stack[-1]:
                stack.pop()
            else:
                break
        stack.append(val)
    
    return res
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a_count = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = andXorOr(a)

    fptr.write(str(result) + '\n')

    fptr.close()
