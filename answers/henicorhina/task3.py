# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""
BIOL7800 assignment 6
Oscar Johnson 9 February 2016
"""

import math
import sys

sys.setrecursionlimit(10000)


def e_recursive_estimator(n=0):
    """
    Estimates Euler's e using recursion
    with no user input
    """
    if n > 1000:
        return 0 
    else:
        n+=1
        return (1/math.factorial(n-1)) + e_recursive_estimator(n)


def main():
    print(e_recursive_estimator())


if __name__ == '__main__':
    main()
