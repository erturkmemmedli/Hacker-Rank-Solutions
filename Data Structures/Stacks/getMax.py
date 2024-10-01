# Maximum Element


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getMax' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts STRING_ARRAY operations as parameter.
#


def getMax(operations):
    # Write your code here
    stack = []
    m = []
    ans = []
    
    for op in operations:
        ops = op.split()
        if len(ops) == 2:
            val = int(ops[1])
            stack.append(val)
            m.append(val if not m or (val > m[-1]) else m[-1])
        elif op == '2':
            stack.pop()
            m.pop()
        else:
            ans.append(m[-1])
    
    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    ops = []

    for _ in range(n):
        ops_item = input()
        ops.append(ops_item)

    res = getMax(ops)

    fptr.write('\n'.join(map(str, res)))
    fptr.write('\n')

    fptr.close()
