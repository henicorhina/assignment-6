#!/usr/bin/env python
# encoding: utf-8

import sys
import math
sys.setrecursionlimit(1100)

y = int(input("To what factorial should e be calculated: "))

def recursion_e(x):
	if x == y:
		return 0
	else:
		return ((1/math.factorial(x)) + recursion_e(x+1))

def main():
	x = 0
	answer = recursion_e(x)
	print(answer)

if __name__ ==  '__main__':
    main()