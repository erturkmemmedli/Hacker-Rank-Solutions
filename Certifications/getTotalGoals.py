# 1. REST API: Total Goals by a Team

#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'getTotalGoals' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING team
#  2. INTEGER year
#

import json
import urllib.parse
import urllib.request


def getTotalGoals(team, year):
    # Write your code here
    base = "https://jsonmock.hackerrank.com/api/football_matches"
    total = 0

    for side in ("team1", "team2"):
        goals_key = side + "goals"
        page, total_pages = 1, 1
        while page <= total_pages:
            qs = urllib.parse.urlencode({"year": year, side: team, "page": page})
            with urllib.request.urlopen(f"{base}?{qs}") as r:
                body = json.loads(r.read().decode())
            total_pages = body.get("total_pages", 1)
            for m in body.get("data", []):
                total += int(m[goals_key])
            page += 1

    return total    


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    team = input()

    year = int(input().strip())

    result = getTotalGoals(team, year)

    fptr.write(str(result) + '\n')

    fptr.close()
