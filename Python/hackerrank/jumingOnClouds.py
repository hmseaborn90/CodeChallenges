#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    jumps = 0
    cur_cloud = 0
    while cur_cloud < len(c):
        if cur_cloud+2 <len(c) and c[cur_cloud+2]==0:
            jumps+=1
            cur_cloud+=2
        elif cur_cloud+1<len(c) and c[cur_cloud+1]==0:
            jumps+=1
            cur_cloud+=1
        else:
            cur_cloud+=1
    return jumps
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()