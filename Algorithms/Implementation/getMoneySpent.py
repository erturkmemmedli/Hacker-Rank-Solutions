# Electronics Shop


#!/bin/python3

import os
import sys

from heapq import heappush, heappop

#
# Complete the getMoneySpent function below.
#
def getMoneySpent(keyboards, drives, b):
    #
    # Write your code here.
    #
    keyboards.sort()
    drives.sort()
    heap = []
    most_expensive = -1
    
    for i in range(len(keyboards)):
        heappush(heap, (keyboards[i] + drives[0], i, 0))
        
    while heap:
        price, key_idx, dr_idx = heappop(heap)
        if price > b:
            break
        
        most_expensive = price
        
        if dr_idx + 1 < len(drives):
            heappush(heap, (keyboards[key_idx] + drives[dr_idx + 1], key_idx, dr_idx + 1))
    
    return most_expensive

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    bnm = input().split()

    b = int(bnm[0])

    n = int(bnm[1])

    m = int(bnm[2])

    keyboards = list(map(int, input().rstrip().split()))

    drives = list(map(int, input().rstrip().split()))

    #
    # The maximum amount of money she can spend on a keyboard and USB drive, or -1 if she can't purchase both items
    #

    moneySpent = getMoneySpent(keyboards, drives, b)

    fptr.write(str(moneySpent) + '\n')

    fptr.close()
