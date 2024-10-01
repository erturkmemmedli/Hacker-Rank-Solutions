# Append and Delete


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'appendAndDelete' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. STRING t
#  3. INTEGER k
#

def appendAndDelete(s, t, k):
    # Write your code here
    match = 0
    
    for i in range(min(len(s), len(t))):
        if s[i] == t[i]:
            match += 1
        else:
            break
            
    s_delete = len(s) - match
    t_add = len(t) - match
    total = s_delete + t_add
        
    return "Yes" if total <= k and ((k - total) % 2 == 0 or len(s) + len(t) <= k) else "No"
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    t = input()

    k = int(input().strip())

    result = appendAndDelete(s, t, k)

    fptr.write(result + '\n')

    fptr.close()
