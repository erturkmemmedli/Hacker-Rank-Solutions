# Strong Password


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumNumber' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. STRING password
#

def minimumNumber(n, password):
    # Return the minimum number of characters to make the password strong    
    digit = 0
    upper = 0
    lower = 0
    special = 0
    required = 0
    
    for char in password:
        if char.isdigit():
            digit += 1
        elif char.isupper():
            upper += 1
        elif char.islower():
            lower += 1
        else:
            special += 1
        
    if not digit:
        required += 1
    if not upper:
        required += 1
    if not lower:
        required += 1
    if not special:
        required += 1
    
    return required if required + n >= 6 else 6 - n
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    password = input()

    answer = minimumNumber(n, password)

    fptr.write(str(answer) + '\n')

    fptr.close()
