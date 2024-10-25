# Sherlock and the Valid String


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'isValid' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

from collections import Counter


def isValid(s):
    # Write your code here
    c = Counter(s)
    val1 = val2 = None
    cnt1 = cnt2 = 0

    for k, v in c.items():
        if val1 is None:
            val1 = v
            cnt1 = 1
        elif val1 == v:
            cnt1 += 1
        elif val2 is None:
            val2 = v
            cnt2 = 1
        elif val2 == v:
            cnt2 += 1
        else:
            return "NO"
    
    if val2 == None:
        return "YES" 
    if (cnt1 == 1 or cnt2 == 1) and abs(val1 - val2) == 1:
        return "YES" 
    if (val1 == 1 and cnt1 == 1) or (val2 == 1 and cnt2 == 1):
        return "YES" 
    else:
        return "NO"
    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()
