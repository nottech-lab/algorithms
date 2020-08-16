#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the powerSum function below.
def powerSum(X, N):
    n=int(X**(1/N))
    return findCount(X,N,1,n)


def findCount(X,N,j,n):
    if(X<0): 
        return 0
    if(X==0):
        return 1
    #n=int(X**(1/N))
    ret=0
    for i in range(j,n+1): 
        k=i**N
        Y=X-k
        ret+=findCount(Y,N,i+1,n)
    return ret

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    X = int(input())

    N = int(input())

    result = powerSum(X, N)

    fptr.write(str(result) + '\n')

    fptr.close()
