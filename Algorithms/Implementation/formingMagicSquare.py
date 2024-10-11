# Forming a Magic Square


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'formingMagicSquare' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY s as parameter.
#

class Solution:
    def formingMagicSquare(self, s):
        # Write your code here
        self.result = float('inf')
        nums = list(range(1, 10))
        self.combination(nums, s, [])
        return self.result
    
    def combination(self, nums, s, path):
        if len(path) == 9:
            if (path[3] + path[4] + path[5] == 15 and
                path[6] + path[7] + path[8] == 15 and
                path[0] + path[3] + path[6] == 15 and
                path[1] + path[4] + path[7] == 15 and
                path[2] + path[5] + path[8] == 15 and
                path[0] + path[4] + path[8] == 15 and 
                path[2] + path[4] + path[6] == 15):
                self.result = min(self.result, 
                    abs(path[0] - s[0][0]) + abs(path[1] - s[0][1]) +  abs(path[2] - s[0][2]) + 
                    abs(path[3] - s[1][0]) + abs(path[4] - s[1][1]) +  abs(path[5] - s[1][2]) + 
                    abs(path[6] - s[2][0]) + abs(path[7] - s[2][1]) +  abs(path[8] - s[2][2])
                )
            return
            
        for i in range(len(nums)):
            self.combination(nums[:i] + nums[i+1:], s, path + [nums[i]])
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = []

    for _ in range(3):
        s.append(list(map(int, input().rstrip().split())))
    
    solution = Solution()
    result = solution.formingMagicSquare(s)

    fptr.write(str(result) + '\n')

    fptr.close()
