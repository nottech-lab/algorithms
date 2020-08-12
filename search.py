'''

'''
import math
import os
import random
import re
import sys

def icecreamParlor(m, a,n):
    d={}
    k=1
    for i in a:
        s=m-i
        if s in d:
            return d[s],k
        else:
            d[i]=k
        k=k+1  
if __name__ == "__main__":
    t = int(input().strip())
    for a0 in range(t):
        m = int(input().strip())
        n = int(input().strip())
        arr = list(map(int, input().strip().split(' ')))
        result = icecreamParlor(m, arr,n)
        print (" ".join(map(str, result)))