# Waiter


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'waiter' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY number
#  2. INTEGER q
#

def prime_numbers(n):
    primes = []
    non_primes = set()
    
    for i in range(2, n + 1):
        if i not in non_primes:
            primes.append(i)
            for j in range(1, n + 1):
                if i * j > n:
                    break
                non_primes.add(i * j)
            
    return primes


def waiter(number, q):
    # Write your code here
    primes = prime_numbers(10000)
    answer = []

    for i in range(q):
        repeat = []
        done = []

        while number:
            num = number.pop()
            
            if num % primes[i] == 0:
                done.append(num)
            else:
                repeat.append(num)
                
                    
        number = repeat[:]
        answer.extend(done[::-1])
    
    answer.extend(number[::-1])
    return answer

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    q = int(first_multiple_input[1])

    number = list(map(int, input().rstrip().split()))

    result = waiter(number, q)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
