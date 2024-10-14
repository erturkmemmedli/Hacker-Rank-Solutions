# Bigger is Greater


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'biggerIsGreater' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING w as parameter.
#

def biggerIsGreater(w):
    # Write your code here
    i = len(w) - 1
    search = None
    found = None
    
    while i >= 1:
        if w[i] > w[i - 1]:
            i -= 1
            search = w[i]
            break
        i -= 1
    else:
        return "no answer"
                
    remaining = sorted(w[i:])
    for j, char in enumerate(remaining):
        if char == search:
            while remaining[j] == char:
                j += 1
            found = j
            break
                
    return w[:i] + remaining[found] + "".join(remaining[:found] + remaining[found + 1:])
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input().strip())

    for T_itr in range(T):
        w = input()

        result = biggerIsGreater(w)

        fptr.write(result + '\n')

    fptr.close()
    
