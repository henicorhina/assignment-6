# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""
BIOL7800 assignment 6
Oscar Johnson 9 February 2016
"""
import math
import sys
sys.setrecursionlimit(10000)



def e_recursive_estimator(n = 0, limit = 0):

    """
    estimates Euler's e using recursion
    user input of the upper limit over which to estimate e
    """
    
    if n == 0:
        limit2 = int(input("enter maximum value for recursion: "))
        return (1/math.factorial(n)) + e_recursive_estimator(n+1, limit2)
 
    elif n <= limit:
        return (1/math.factorial(n)) + e_recursive_estimator(n+1, limit)
        
    else:
        return 0


def main():
    print (e_recursive_estimator())


if __name__ == '__main__':
    main()
