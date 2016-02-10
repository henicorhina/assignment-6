# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""
BIOL7800 assignment 6
Oscar Johnson 9 February 2016
"""
import math
import sys
sys.setrecursionlimit(10000)



def e_recursive_estimator(n = 0):

    if n > 1000:
        return 0
 
    else:
        #n -= 1
        return (1/math.factorial(n)) + e_recursive_estimator(n+1)


def main():
    print (e_recursive_estimator())


if __name__ == '__main__':
    main()
