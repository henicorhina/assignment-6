# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""
BIOL7800 assignment 6
Oscar Johnson 9 February 2016
"""


def recurse_sum(max_val = 100):
    """
    returns the sum of the numbers from zero to the max_val
    using recursion
    """
    if max_val <= 1:
        return max_val
    else:
        return max_val + recurse_sum(max_val - 1)


def main():
    print (recurse_sum())


if __name__ == '__main__':
    main()
