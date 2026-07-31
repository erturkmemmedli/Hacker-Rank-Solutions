# Problem Solving (Intermediate): 2. Task of Pairing

#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'taskOfPairing' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER_ARRAY freq as parameter.
#

def taskOfPairing(freq):
    # Write your code here
    pairs = 0
    carry = 0
    for f in freq:
        if f == 0:
            carry = 0
            continue
        f += carry
        pairs += f // 2
        carry = f % 2
    return pairs


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    freq_count = int(input().strip())

    freq = []

    for _ in range(freq_count):
        freq_item = int(input().strip())
        freq.append(freq_item)

    result = taskOfPairing(freq)

    fptr.write(str(result) + '\n')

    fptr.close()
