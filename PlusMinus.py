#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    p=0
    ne=0
    z=0
    for i in range(n):
        if arr[i]<0:
            ne+=1
        elif arr[i]>0:
            p+=1
        else:
            z+=1
    pos = p/n
    neg = ne/n
    zer = z/n 
    print(pos)
    print(neg)
    print(zer)
            
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
