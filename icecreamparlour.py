#https://www.hackerrank.com/challenges/icecream-parlor/problem

#!/bin/python

import math
import os
import random
import re
import sys

# Complete the icecreamParlor function below.
def icecreamParlor(m, arr):
    for i,cost in enumerate(arr):
        if (m-cost) in arr[i+1:]:
            return (i+1, arr[i+1:].index(m-cost)+i+2)
 
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(raw_input())

    for t_itr in xrange(t):
        m = int(raw_input())

        n = int(raw_input())

        arr = map(int, raw_input().rstrip().split())

        result = icecreamParlor(m, arr)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()