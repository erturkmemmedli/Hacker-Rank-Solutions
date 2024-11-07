# Mr. X and His Shots


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'solve' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. 2D_INTEGER_ARRAY shots
#  2. 2D_INTEGER_ARRAY players
#

from bisect import bisect_left, bisect_right

def solve(shots, players):
    # Write your code here
    shots.sort(key=lambda x: x[0])
    begins = [r[0] for r in shots]
    
    shots.sort(key=lambda x: x[1])
    ends = [r[1] for r in shots]
    
    ans = len(shots) * len(players)
    
    for p in players:
        x = bisect_left(ends, p[0])
        y = len(ends) - bisect_right(begins, p[1])
        
        ans -= x
        ans -= y
        
    return ans


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    shots = []

    for _ in range(n):
        shots.append(list(map(int, input().rstrip().split())))

    players = []

    for _ in range(m):
        players.append(list(map(int, input().rstrip().split())))

    result = solve(shots, players)

    fptr.write(str(result) + '\n')

    fptr.close()
