# The Time in Words


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeInWords' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER h
#  2. INTEGER m
#

def timeInWords(h, m):
    # Write your code here
    H = {
        1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight',
        9: 'nine', 10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen',
        16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen', 20: 'twenty'
    }
    
    if m == 0:
        return H[h] + " o' clock"
    elif m == 1:
        return H[m] + " minute past " + H[h]
    elif m == 59:
        return H[60 - m] + " minute to " + H[h + 1 if h != 12 else 1]
    elif m == 15:
        return "quarter past " + H[h]
    elif m == 45:
        return "quarter to " + H[h + 1 if h != 12 else 1]
    elif m == 30:
        return "half past " + H[h]
    elif m <= 20:
        return H[m] + " minutes past " + H[h]
    elif m >= 40:
        return H[60 - m] + " minutes to " + H[h + 1 if h != 12 else 1]
    elif 20 < m < 30:
        return H[20] + " " + H[m - 20] + " minutes past " + H[h]
    else:
        return H[20] + " " + H[40 - m] + " minutes to " + H[h + 1 if h != 12 else 1]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = int(input().strip())

    m = int(input().strip())

    result = timeInWords(h, m)

    fptr.write(result + '\n')

    fptr.close()
