#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the superReducedString function below.
def superReducedString(s):
    current = 0
    while current < len(s) - 1:
        if s[current] == s[current+1]:
            s = s[:current] + s[current+2:]
            current = 0
        else:
            current += 1
    return s if s else 'Empty String'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = superReducedString(s)

    fptr.write(result + '\n')

    fptr.close()
