# Modified Kaprekar Numbers


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'kaprekarNumbers' function below.
#
# The function accepts following parameters:
#  1. INTEGER p
#  2. INTEGER q
#

def kaprekarNumbers(p, q):
    # Write your code here
    result = []
    
    for i in range(p, q + 1):
        d = findDigitCount(i)
        sq_num = i ** 2
        right = sq_num % (10 ** d)
        left = sq_num // (10 ** d)
        if i == left + right:
            result.append(i)
        
    if result:
        print(*result)
    else:
        print("INVALID RANGE")
    
    
def findDigitCount(n):
    count = 0
    while n:
        count += 1
        n //= 10
    return count
    

if __name__ == '__main__':
    p = int(input().strip())

    q = int(input().strip())

    kaprekarNumbers(p, q)
