"""CodeChallenge: implicit differentiation

COURSE: Master calculus 1 using Python: derivatives and applications
SECTION: Differentiation rules and theorems
LECTURE: CodeChallenge: implicit differentiation
"""
import numpy as np
import sympy as sym
import matplotlib.pyplot as plt

# Exercise 1: Implicit differentiation in sympy

# create two symbolic variables
x, y = sym.symbols('x, y')

# define expression (implicitly set to 0!)
expr = x*y-1

# implicit differentiation (input order is expression, y, x)
sym.idiff(expr, y, x)

# now plot
sym.plot_implicit(expr, (x, -2, 3), (y, -4, 2));
sym.plot_implicit(sym.idiff(expr, y, x))

solve4y = sym.solve(expr, y)
df = sym.idiff(expr, y, x).subs(y, solve4y[0])
sym.plot(df, xlim=(-3, 3), ylim=(-10, 1))

# Exercise 2: Evaluate expression at a value

# expression
expr = x**3 * y**2 - 5*x**4

# derivative via implicit differentiation
sym.idiff(expr, y, x)

# substitute a symbolic variable for y
num2evalY = sym.sqrt(5)
sym.idiff(expr, y, x).subs(y, num2evalY)

# substitute a numerical value for y
num2evalY = np.sqrt(5)
sym.idiff(expr, y, x).subs(y, num2evalY)

# substitute symbolic variables for x and y
num2evalX = sym.sqrt(5)
num2evalY = sym.pi
sym.idiff(expr, y, x).subs([ (x, num2evalX), (y, num2evalY) ])

# substitute numerical variables for x and y
num2evalX = np.sqrt(5)
num2evalY = np.pi
sym.idiff(expr, y, x).subs([ (x, num2evalX), (y, num2evalY) ])

# Exercise 3: Derivative without a function

# expression and its derivative
expr = sym.exp(x**2+y**2) - x - y
sym.idiff(expr, y, x)

# plots
sym.plot_implicit(expr);
sym.plot_implicit(sym.idiff(expr, y, x), (x, 0, .5), (y, -3, 3));

# try to solve for y
sym.solve(expr, y)

# try to solve for y
sym.solve(sym.idiff(expr, y, x), y)

