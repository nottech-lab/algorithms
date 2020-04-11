#https://www.hackerrank.com/challenges/grading/submissions/code/152522736

#!/bin/python
import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    for i, grade in enumerate(grades):
        if grade < 38:
            continue
        if (grade + 1)%5 == 0:
            grades[i] = grade + 1
        elif (grade + 2)%5 == 0:
            grades[i] = grade + 2
    
    return grades
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(raw_input().strip())

    grades = []

    for _ in xrange(grades_count):
        grades_item = int(raw_input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()