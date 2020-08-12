'''
This is sorting in algorithms
'''

#!/bin/python

import math
import os
import random
import re
import sys


def bigSorting(unsorted):
    

    if __name__ == '__main__':
        fptr = open(os.environ['OUTPUT_PATH'], 'w')

        n = int(raw_input())

        unsorted = []

        for _ in xrange(n):
            unsorted_item = raw_input()
            unsorted.append(unsorted_item)

        result = bigSorting(unsorted)

        fptr.write('\n'.join(result))
        fptr.write('\n')

        fptr.close()