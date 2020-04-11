#https://www.hackerrank.com/challenges/camelcase/problem

#!/bin/python

import math
import os
import random
import re
import sys

# Complete the camelcase function below.
def camelcase(s):
    count = 1
    for i in range(1, len(s) - 1):
        if (s[i].isupper()):
            count += 1

    return count        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = raw_input()

    result = camelcase(s)

    fptr.write(str(result) + '\n')

    fptr.close()