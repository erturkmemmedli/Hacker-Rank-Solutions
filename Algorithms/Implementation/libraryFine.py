# Library Fine


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'libraryFine' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER d1
#  2. INTEGER m1
#  3. INTEGER y1
#  4. INTEGER d2
#  5. INTEGER m2
#  6. INTEGER y2
#

from datetime import datetime


def libraryFine(d1, m1, y1, d2, m2, y2):
    # Write your code here
    return_date = datetime(y1, m1, d1)
    due_date = datetime(y2, m2, d2)
    
    if return_date <= due_date:
        return 0
    elif return_date.year == due_date.year and return_date.month == due_date.month:
        return 15 * (return_date.day - due_date.day)
    elif return_date.year == due_date.year:
        return 500 * (return_date.month - due_date.month)
    else:
        return 10000


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    d1 = int(first_multiple_input[0])

    m1 = int(first_multiple_input[1])

    y1 = int(first_multiple_input[2])

    second_multiple_input = input().rstrip().split()

    d2 = int(second_multiple_input[0])

    m2 = int(second_multiple_input[1])

    y2 = int(second_multiple_input[2])

    result = libraryFine(d1, m1, y1, d2, m2, y2)

    fptr.write(str(result) + '\n')

    fptr.close()
