#!/bin/python

import math
import os
import random
import re
import sys

from collections import Counter
#
# Complete the 'isValid' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def isValid(s):
    c = Counter(s)
    if len(set(c.values())) == 1:
        return "YES"
    elif len(set(c.values())) > 2:
        return "NO"
    else:
        m1 = max(c.values())
        m2 = min(c.values())
        if c.values().count(m2) == 1:
            return "YES"
        if c.values().count(m1) > 1 or m1 - m2 > 1:
            return "NO"
        return "YES"
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = raw_input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()
