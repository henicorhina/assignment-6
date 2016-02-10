# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""
BIOL7800 assignment 6
Oscar Johnson 9 February 2016
"""

import argparse
import math
import sys

sys.setrecursionlimit(10000)


def get_args():
    parser = argparse.ArgumentParser(
                description="use recursion to estimate Euler's e"
                )
    
    parser.add_argument(
                "-- recursion_depth",
                dest = "recursion_depth",
                type = int
                )
    return parser.parse_args()

def e_recursive_estimator(n = 0, recursion_depth = 0):

    """
    estimates Euler's e using recursion
    """
    limit = 0
    if n == 0:
        return (1/math.factorial(n)) + e_recursive_estimator(n+1, recursion_depth)
 
    elif n <= limit:
        return (1/math.factorial(n)) + e_recursive_estimator(n+1, limit)
        
    else:
        return 0


def main():
    args = get_args()
    print (e_recursive_estimator(args))


if __name__ == '__main__':
    main()
