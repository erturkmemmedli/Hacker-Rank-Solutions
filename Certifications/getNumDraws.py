# 2. REST API: Number of Drawn Matches

#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'getNumDraws' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER year as parameter.
#

import json
import urllib.request

def getNumDraws(year):
    # Write your code here
    base = "https://jsonmock.hackerrank.com/api/football_matches"
    total = 0
    for g in range(11):
        url = f"{base}?year={year}&team1goals={g}&team2goals={g}&page=1"
        with urllib.request.urlopen(url) as r:
            total += json.loads(r.read().decode()).get("total", 0)
    return total
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    year = int(input().strip())

    result = getNumDraws(year)

    fptr.write(str(result) + '\n')

    fptr.close()
