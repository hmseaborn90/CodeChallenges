#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the staircase function below.
def staircase(n):
    spaces = n-1
    stairs = 1
    while n: 
        print(" "*spaces + '#'*stairs)
        n -= 1
        spaces -= 1
        stairs += 1        
print(staircase(6))
