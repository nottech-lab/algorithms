
'''
    Graph theory challenge
'''
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the roadsAndLibraries function below.

def roadsAndLibraries(n, c_lib, c_road, cities):
    if c_lib<=c_road: return c_lib * n
    pre=[-1]*n
    cost=0
    for road in cities:
        u=road[0]-1
        v=road[1]-1
        while True:
            if pre[u]==-1 and pre[v]==-1 and u!=v:
                cost+=c_road
                pre[v]=u
            elif pre[u]>-1 and pre[v]==-1:
                u=pre[u]
            elif pre[u]==-1 and pre[v]>-1:
                v=pre[v]
            elif pre[u]==pre[v]:
                break
            else:
                u=pre[u]
                v=pre[v]
    ends=0
    for k in pre:
        if k==-1:
            ends+=1
    return cost+(c_lib*ends)

       
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        nmC_libC_road = input().split()

        n = int(nmC_libC_road[0])

        m = int(nmC_libC_road[1])

        c_lib = int(nmC_libC_road[2])

        c_road = int(nmC_libC_road[3])

        cities = []

        for _ in range(m):
            cities.append(list(map(int, input().rstrip().split())))

        result = roadsAndLibraries(n, c_lib, c_road, cities)

        fptr.write(str(result) + '\n')

    fptr.close()
