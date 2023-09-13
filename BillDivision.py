'''Two friends Anna and Brian, are deciding how to split the bill at a dinner. 
Each will only pay for the items they consume. Brian gets the check and calculates Anna's portion. You must determine if his calculation is correct.'''

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'bonAppetit' function below.
#
# The function accepts following parameters:
#  1. INTEGER_ARRAY bill
#  2. INTEGER k
#  3. INTEGER b
#

def bonAppetit(bill, k, b):
    #Write your code here
    if (sum(bill)-bill[k])/2 == b:
        print('Bon Appetit')
    else:
        print(int(b-((sum(bill)-bill[k])/2)))
    # sum=0
    # for i in range(len(bill)):
    #     sum+=bill[i]
    # if (sum-bill[k])//2 == b:
    #     print('Bon Appetit')
    # else:
    #     print(int(b-(sum-bill[k])//2))
        
        
            
        
    

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    bill = list(map(int, input().rstrip().split()))

    b = int(input().strip())

    bonAppetit(bill, k, b)
