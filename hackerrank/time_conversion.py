# Time Complexity - O(1)
# Space Complexity - O(1)

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Extract AM/PM
    modifier = s[-2:]
    # Extract the hour part
    hour = int(s[:2])
    # Extract the rest of the time (minutes and seconds)
    rest = s[2:-2]
    
    if modifier == "PM":
        if hour != 12:
            hour += 12
    else: # AM case
        if hour == 12:
            hour = 0
            
    # Format the hour back to a 2-digit string and combine
    return f"{hour:02}{rest}"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
