# Fraudulent Activity Notifications


#!/bin/python3

import math
import os
import random
import re
import sys

from heapq import heappush, heappop

#
# Complete the 'activityNotifications' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY expenditure
#  2. INTEGER d
#

def activityNotifications(expenditure, d):
    # Write your code here
    min_heap = []
    max_heap = []
    out_of_window = {num : 0 for num in expenditure}
    count = 0

    for i in range(d):
        if not max_heap or expenditure[i] <= -max_heap[0]:
            heappush(max_heap, -expenditure[i])
        else:
            heappush(min_heap, expenditure[i])
        
        if len(max_heap) > len(min_heap) + 1:
            heappush(min_heap, -heappop(max_heap))
        if len(max_heap) < len(min_heap):
            heappush(max_heap, - heappop(min_heap))
        
    for i in range(d, len(expenditure)):
        median = -max_heap[0] if d & 1 else (min_heap[0] - max_heap[0]) / 2
        
        if expenditure[i] >= median * 2:
            count += 1

        remove, add = expenditure[i - d], expenditure[i]
        out_of_window[remove] += 1
        balance = 0

        if remove <= -max_heap[0]:
            balance -= 1
        else:
            balance += 1
        
        if not max_heap or add <= -max_heap[0]:
            balance += 1
            heappush(max_heap, -add)
        else:
            balance -= 1
            heappush(min_heap, add)

        if balance > 0:
            heappush(min_heap, -heappop(max_heap))
            balance += 1
        if balance < 0:
            heappush(max_heap, - heappop(min_heap))
            balance -= 1
        
        while max_heap and out_of_window[-max_heap[0]] > 0:
            out_of_window[-max_heap[0]] -= 1
            heappop(max_heap)
        while min_heap and out_of_window[min_heap[0]] > 0:
            out_of_window[min_heap[0]] -= 1
            heappop(min_heap)

    return count
        
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    d = int(first_multiple_input[1])

    expenditure = list(map(int, input().rstrip().split()))

    result = activityNotifications(expenditure, d)

    fptr.write(str(result) + '\n')

    fptr.close()
