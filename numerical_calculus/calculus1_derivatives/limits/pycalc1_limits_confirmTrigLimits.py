"""CodeChallenge: Confirm the trig limits

COURSE: Master calculus 1 using Python: derivatives and applications
SECTION: Limits
LECTURE: CodeChallenge: Confirm the trig limits
"""
import numpy as np
import sympy as sym
import matplotlib.pyplot as plt

# Exercise 1: The important ones

# functions in sympy
phi = sym.symbols('phi')
fx1 = sym.sin(phi) / phi
fx2 = (sym.cos(phi)-1) / phi


# print out limits
print('\nLimit of sin(x)/x as x approaches zero:')
print( sym.limit(fx1, phi, 0, dir='+-') )

print('\nLimit of (cos(x)-1)/x as x approaches zero:')
print( sym.limit(fx2, phi, 0, dir='+-') )

