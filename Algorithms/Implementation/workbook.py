# Lisa's Workbook


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'workbook' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. INTEGER_ARRAY arr
#

def workbook(n, k, arr):
    # Write your code here
    special_page_count = 0
    curr_page = 1
    
    for chapter in range(len(arr)):
        problem_no = 0
        while problem_no <= arr[chapter]:
            # print('chapter:',chapter+1,'page:',curr_page,'prob:',problem_no)
            if problem_no < curr_page <= min(problem_no + k, arr[chapter]):
                special_page_count += 1
            if problem_no + k < arr[chapter]:
                curr_page += 1
            problem_no += k
        # print('count:',special_page_count)
        curr_page += 1
    
    return special_page_count
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    result = workbook(n, k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
