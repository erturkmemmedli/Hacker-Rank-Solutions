# Matrix Layer Rotation


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'matrixRotation' function below.
#
# The function accepts following parameters:
#  1. 2D_INTEGER_ARRAY matrix
#  2. INTEGER r
#

def matrixRotation(matrix, r):
    # Write your code here
    row_low, row_high = 0, len(matrix) - 1
    col_low, col_high = 0, len(matrix[0]) - 1
    
    while row_low < row_high and col_low < col_high:
        total = 2 * (row_high - row_low + col_high - col_low)
        k = r % total
        circular = []
        helper(circular, matrix, row_low, row_high, col_low, col_high, True)
        circular = circular[-k:] + circular[:-k]
        helper(circular, matrix, row_low, row_high, col_low, col_high, False)
        row_low, row_high, col_low, col_high = row_low + 1, row_high - 1, col_low + 1, col_high - 1

    [print(*m) for m in matrix]
        
        
def helper(arr, mat, r1, r2, c1, c2, create_mode):
    k = 0
    if create_mode:
        for i in range(r1, r2+1):
            arr.append([i, c1, mat[i][c1]])
        for i in range(c1+1, c2+1):
            arr.append([r2, i, mat[r2][i]])
        for i in range(r2-1, r1-1, -1):
            arr.append([i, c2, mat[i][c2]])
        for i in range(c2-1, c1, -1):
            arr.append([r1, i, mat[r1][i]])
    else:
        for i in range(r1, r2+1):
            mat[i][c1] = arr[k][2]
            k += 1
        for i in range(c1+1, c2+1):
            mat[r2][i] = arr[k][2]
            k += 1
        for i in range(r2-1, r1-1, -1):
            mat[i][c2] = arr[k][2]
            k += 1
        for i in range(c2-1, c1, -1):
            mat[r1][i] = arr[k][2]
            k += 1

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    m = int(first_multiple_input[0])

    n = int(first_multiple_input[1])

    r = int(first_multiple_input[2])

    matrix = []

    for _ in range(m):
        matrix.append(list(map(int, input().rstrip().split())))

    matrixRotation(matrix, r)
