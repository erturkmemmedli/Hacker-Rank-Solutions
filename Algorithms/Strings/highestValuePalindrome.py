# Highest Value Palindrome


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'highestValuePalindrome' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER n
#  3. INTEGER k
#

from collections import deque

def highestValuePalindrome(s, n, k):
    # Write your code here
    string = [char for char in s]
    i, j = 0, n - 1
    indices = deque()
    priorities = []
    
    while i < j and k >= 0:
        if int(s[i]) != int(s[j]):
            if s[i] == '9' or s[j] == '9':
                priorities.append((i, j))
            else:
                indices.append((i, j))
        i += 1
        j -= 1
    
    if len(indices) + len(priorities) > k:
        return '-1'
        
    while priorities:
        a, b = priorities.pop()
        k -= 1
        string[a] = string[b] = '9'
    
    i = 0
    while i < n // 2 and (k > 1 or (k > 0 and indices)):
        if string[i] == '9':
            i += 1
            continue
        if len(indices) * 2 <= k:
            if indices and indices[0][0] == i:
                a, b = indices.popleft()
            string[i] = string[-i - 1] = '9'
            k -= 2
            i += 1
        else:
            a, b = indices.pop()
            string[a] = string[b] = max(s[a], s[b])
            k -= 1
    
    if k % 2 == 1 and n % 2 == 1:
        string[n // 2] = '9'
        
    return "".join(string)
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    s = input()

    result = highestValuePalindrome(s, n, k)

    fptr.write(result + '\n')

    fptr.close()
