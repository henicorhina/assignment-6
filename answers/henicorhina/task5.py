# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""
BIOL7800 assignment 6
Oscar Johnson 10 February 2016
"""

import argparse
import math
import sys

sys.setrecursionlimit(1000)


def get_args():
    parser = argparse.ArgumentParser(
                description="""use recursion to estimate Euler's e"""
                )
    
    parser.add_argument(
                "recursion_depth",
                help = "the maximum number of times over which to run the recursive function",
                type = int
                )
    #get_args.recursion_depth
    return parser.parse_args()

def e_recursive_estimator(args, n = 0):

    """
    estimates Euler's e using recursion
    """
    #limit = 0
    args = int(get_args())
    #args = 100    
    if n < args:
        return (1/math.factorial(n)) + e_recursive_estimator(args, n+1)
 
    else:
        return 0

#print (e_recursive_estimator())

def main():
    args = get_args()
    print (e_recursive_estimator(args, 0))
    #pass

if __name__ == '__main__':
    main()
