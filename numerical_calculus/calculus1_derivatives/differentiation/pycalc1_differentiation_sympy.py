"""CodeChallenge: derivatives in sympy

COURSE: Master calculus 1 using Python: derivatives and applications
SECTION: Differentiation fundamentals
LECTURE: CodeChallenge: derivatives in sympy
"""
import numpy as np
import sympy as sym
import matplotlib.pyplot as plt

# Exercise 1: Derivative of a line

# create sympy expression object and plot
x = sym.symbols('x')
fx = (5/4)*x + 9/4
sym.plot(fx, (x, -1, 6), axis_center=[0, 0])

# compute the derivative
sym.diff(fx, x)

# store as a variable
dydx = sym.diff(fx, x)
print(f'The derivative is {dydx}')

# Exercise 2: Derivative of a polynomial

# create sympy expression object and plot
x = sym.symbols('x')
fx = x**2
sym.plot(fx, (x, -1, 6))

# store as a variable
dydx = sym.diff(fx, x)
dydx

# Exercise 3: Plot and query the derivative

sym.plot(dydx, (x, -1, 6))

# query the derivative at a particular point
somePoints = [-1, 0, 2]

for p in somePoints:
  print(f'The derivative at x={p} is dy/dx={dydx.subs(x, p)}')

