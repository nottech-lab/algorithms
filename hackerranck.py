#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hackerrankInString function below.
def hackerrankInString(s):
    l = 'hackerrank'
    x = 0
    for i in range(len(s)):
        if s[i] == l[x]:
            x += 1
            if x == len(l):
                return 'YES'
    return 'NO'        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = hackerrankInString(s)

        fptr.write(result + '\n')

    fptr.close()
