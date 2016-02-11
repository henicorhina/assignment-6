# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""
BIOL7800 assignment 6
Oscar Johnson 10 February 2016
"""

import argparse
import math
import sys

sys.setrecursionlimit(5000)


def get_args():
    parser = argparse.ArgumentParser(
                description="""use recursion to estimate Euler's e"""
                )
    
    parser.add_argument(
                "--recursion_depth",
                dest = "recursion_depth",
                required = True,
                type = int,
                help = "the maximum number of times over which to run the recursive function"
                )
    return parser.parse_args()


def e_recursive_estimator(args, n=0):
    """
    Estimates Euler's e using recursion
    with no user input
    """
    if n > args.recursion_depth:
        return 0 
    else:
        n+=1
        return (1/math.factorial(n-1)) + e_recursive_estimator(args, n)


def main():
    args = get_args()
    print(e_recursive_estimator(args))
    #pass

if __name__ == '__main__':
    main()

