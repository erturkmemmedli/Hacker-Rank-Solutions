# Encryption


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'encryption' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def encryption(s):
    # Write your code here
    space_count = s.count(" ")
    trimmed = len(s) - space_count
    col = int(math.ceil(trimmed ** 0.5))
    answer_list = ["" for _ in range(col)]
    i = 0
    
    for char in s:
        if char != " ":
            answer_list[i % col] += char
            i += 1
    
    return " ".join(answer_list)
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = encryption(s)

    fptr.write(result + '\n')

    fptr.close()
