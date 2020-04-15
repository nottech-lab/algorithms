import math
import os
import random
import re
import sys

# Complete the andProduct function below.
def andProduct(a, b):
    ans = 0
    for i in range(32):
        if((a>>i)&1):
            x = (2**i) - (a&((2**i)-1))
            if(x >= (b - a + 1)):
                ans = ans + 2**i
    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    for n_itr in range(n):
        ab = input().split()

        a = int(ab[0])

        b = int(ab[1])

        result = andProduct(a, b)

        fptr.write(str(result) + '\n')

    fptr.close()