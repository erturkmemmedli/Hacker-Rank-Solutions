# Sam and substrings


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'substrings' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING n as parameter.
#

'''
df(n) = 10 * df(n-1) + n * digits[n]
f(n) = f(n-1) + df(n)
'''

def substrings(n):
    # Write your code here
    mod = 10**9 + 7
    fn = int(n[0])
    dfn = int(n[0])
    
    for i in range(1, len(n)):
        dfn = (10 * dfn + (i + 1) * int(n[i])) % mod
        fn = (fn + dfn) % mod
        
    return fn

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = input()

    result = substrings(n)

    fptr.write(str(result) + '\n')

    fptr.close()
