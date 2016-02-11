# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""
BIOL7800 assignment 6
Oscar Johnson 9 February 2016
"""

import math
import sys

sys.setrecursionlimit(5000)


def e_recursive_estimator(limit, n=0):
    """
    Estimates Euler's e using recursion
    with no user input
    """
    if n > limit:
        return 0 
    else:
        n+=1
        return (1/math.factorial(n-1)) + e_recursive_estimator(limit, n)


def main():
    limit = int(input("enter maximum value for recursion: "))
    print(e_recursive_estimator(limit))


if __name__ == '__main__':
    main()
