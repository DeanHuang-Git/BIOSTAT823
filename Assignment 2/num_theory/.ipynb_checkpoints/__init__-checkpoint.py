from math import pi
from sympy import *
from mpmath import mp

def pi_expansion(digits,num):
    """A function that has a number, 'num', and the number of digits, 'digits', as input. Return the expansion of the number"""
    # Set the number of digits
    mp.dps = digits
    # Return the expansion of the number as output
    return Float(num,digits)