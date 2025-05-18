# Sam and substrings

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'substrings' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING n as parameter.
#

def substrings(s):
    # Write your code here
    n = len(s)
    dp = [0] * n
    result = dp[0] = int(s[0])
    
    for i in range(1, n):
        dp[i] = dp[i-1] * 10 + int(s[i]) * (i+1)
        dp[i] %= 1_000_000_007
        result += dp[i]
        result %= 1_000_000_007
            
    return result
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = input()

    result = substrings(n)

    fptr.write(str(result) + '\n')

    fptr.close()
