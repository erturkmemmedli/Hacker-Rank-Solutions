# Software Engineer: 3 - REST API: Patent's Medical Record

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getAverageTemperatureForUser' function below.
#
# URL for cut and paste
# https://jsonmock.hackerrank.com/api/medical_records?userId=<userId>&page=<page>
#
# The function is expected to return a String value.
# The function accepts a userId argumnent (Integer).
# In the case of an empty array result, return value '0'
#

import json
import urllib.request

def getAverageTemperatureForUser(userId):
    # Write your code here
    base = "https://jsonmock.hackerrank.com/api/medical_records"
    temps = []
    page, total_pages = 1, 1

    while page <= total_pages:
        with urllib.request.urlopen(f"{base}?userId={userId}&page={page}") as r:
            body = json.loads(r.read().decode())
            
        total_pages = body.get("total_pages", 1)
        for rec in body.get("data", []):
            t = rec.get("vitals", {}).get("bodyTemperature")
            if t is not None:
                temps.append(t)

        page += 1

    return "0" if not temps else f"{sum(temps) / len(temps):.1f}"
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    userId = int(input().strip())

    result = getAverageTemperatureForUser(userId)

    fptr.write(result + '\n')

    fptr.close()
