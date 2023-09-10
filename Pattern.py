#1
n = int(input())
for row in range(1, n+1):
    for col in range(1, row+1):
        print('*',end='')
    print()

#2
n = int(input())
for row in range(n,0,-1):
    for col in range(1, row+1):
        print('*',end='')
    print()

n = int(input())
for row in range(1, n+1):
    for col in range(1,row+1):
        print('* ',end='')
    print()
for row in range(n-1,0,-1):
    for j in range(1,row+1):
        print('* ', end='')
    print()

#3
#hacker-rank with built in
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'staircase' function below.
#
# The function accepts INTEGER n as parameter.
#

def staircase(n):
    # Write your code here
    for row in range(1, n + 1):
        print(('#'*row).rjust(n))

if __name__ == '__main__':
    n = int(input().strip())

    staircase(n)
