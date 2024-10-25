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

def highestValuePalindrome(s, n, k):
    # Write your code here
    string = [char for char in s]
    i, j = 0, n - 1
    indices = []
    
    while i < j and k >= 0:
        if int(s[i]) != int(s[j]):
            indices.append((i, j))
        i, j = i + 1, j - 1
    
    if len(indices) > k:
        return '-1'
        
    while len(indices) * 2 > k:
        a, b = indices.pop()
        k -= 1
        string[a], string[b] = max(s[a], s[b]), max(s[a], s[b])
    
    i, count = 0, k // 2
    while i < n // 2 and count > 0:
        if string[i] != '9' or string[-i - 1] != '9':
            string[i] = '9'
            string[-i - 1] = '9'
            count -= 1
        i += 1
        
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
