# Two Characters


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'alternate' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

import string


def alternate(s):
    # Write your code here
    maximum = 0
    
    if len(s) == 1:
        return 0
    
    for i in range(25):
        for j in range(i + 1, 26):
            first = chr(ord('a') + i)
            second = chr(ord('a') + j)
            alter = ""
            
            for char in s:
                if (char == first or char == second):
                    if not alter or alter[-1] != char:
                        alter += char
                    else:
                        break
            else:
                maximum = max(maximum, len(alter))
                
    return maximum

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    l = int(input().strip())

    s = input()

    result = alternate(s)

    fptr.write(str(result) + '\n')

    fptr.close()
