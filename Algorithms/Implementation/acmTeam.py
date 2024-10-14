# ACM ICPC Team


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'acmTeam' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts STRING_ARRAY topic as parameter.
#

def acmTeam(topic):
    # Write your code here
    total = 0
    max_count = 0
    n = len(topic)
    m = len(topic[0])
    
    for i in range(n):
        for j in range(i + 1, n):
            count = 0
            for k in range(m):
                if topic[i][k] == '1' or topic[j][k] == '1':
                    count += 1
            if count > max_count:
                max_count = count
                total = 1
            elif count == max_count:
                total += 1
                
    return [max_count, total]
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    topic = []

    for _ in range(n):
        topic_item = input()
        topic.append(topic_item)
    result = acmTeam(topic)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
