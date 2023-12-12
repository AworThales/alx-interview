#!/usr/bin/python3
""" Module for 0-minoperations"""


def minOperations(n):
    """
    minOperations
    Gets fewest # of operations needed to result in exactly n H characters
    """
    # all outputs should be at least 2 char: (min, Copy All => Paste)
    if (n < 2):
        return 0
    num1, value = 0, 2
    while value <= n:
        # if n evenly divides by value
        if n % value == 0:
            # total even-divisions by value = total operations
            num1 += value
            # set n to the remainder
            n = n / value
            # reduce value to find remaining smaller vals that evenly-divide n
            value -= 1
        # increment value until it evenly-divides n
        value += 1
    return num1
