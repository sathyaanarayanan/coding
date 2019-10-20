#!/bin/python

## Given an integer,n,perform the following conditional actions:
## If is n odd, print Weird
## If n is even and in the inclusive range of 2 to 5, print Not Weird
## If n is even and in the inclusive range of 6 to 20, print Weird
## If n is even and greater than 20, print Not Weird


import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(raw_input().strip())
    isOdd = n &((1<<1)-1)  #picks up the last bit of the int n
    if isOdd:
        print("Weird")
    elif isOdd==0:
        if n in range (2,5):
            print "Not Weird"
        elif n in range (6,20):
            print "Weird"
        elif n > 20:
            print "Not Weird"