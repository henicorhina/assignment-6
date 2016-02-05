#!/usr/bin/env python
# encoding: utf-8

import sys
import math
sys.setrecursionlimit(1100)

def recursion_e(x):
    if x == 1000:
        return 0
    else:
        return ((1/math.factorial(x)) + recursion_e(x+1))

def main():
    answer = recursion_e(0)
    print(answer)

if __name__ ==  '__main__':
    main()