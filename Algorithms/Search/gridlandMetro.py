# Gridland Metro


#!/bin/python3

import math
import os
import random
import re
import sys

from bisect import bisect_left, bisect_right

#
# Complete the 'gridlandMetro' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
#  3. INTEGER k
#  4. 2D_INTEGER_ARRAY track
#

def merge_interval(intervals, new_interval):
    result = []
    i = 0
    while i < len(intervals):
        if intervals[i][0] < new_interval[0]:
            result.append(intervals[i])
            i += 1
        else:
            break
    if result and new_interval[0] <= result[-1][1]:
        result[-1][1] = max(result[-1][1], new_interval[1])
    else:
        result.append(new_interval)
    for current in intervals[i:]:
        last = result[-1]
        if current[0] > last[1]:
            result.append(current)
        else:
            start = last[0]
            end = max(last[1], current[1])
            result[-1] = [start, end]
    return result
        


def gridlandMetro(n, m, k, track):
    # Write your code here
    total = n * m
    hashmap = {}
    
    for r, c1, c2 in track:
        hashmap[r] = merge_interval(hashmap[r] if r in hashmap else [], [c1, c2])
        
    for intervals in hashmap.values():
        for interval in intervals:
            total -= (interval[1] - interval[0] + 1)

    return total

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    k = int(first_multiple_input[2])

    track = []

    for _ in range(k):
        track.append(list(map(int, input().rstrip().split())))

    result = gridlandMetro(n, m, k, track)

    fptr.write(str(result) + '\n')

    fptr.close()
