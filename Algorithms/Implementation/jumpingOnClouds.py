# Jumping on the Clouds: Revisited


#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c, k):
    position = 0
    step = 0
    thunder = 0
    flag = False
    
    while position != 0 or not flag:
        if not flag:
            flag = True
            
        position = (position + k) % n
        thunder += c[position]
        step += 1
    
    return 100 - step - 2 * thunder
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c, k)

    fptr.write(str(result) + '\n')

    fptr.close()
