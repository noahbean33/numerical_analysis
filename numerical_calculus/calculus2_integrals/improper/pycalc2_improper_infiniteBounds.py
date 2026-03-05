"""Two infinite bounds

COURSE: Master calculus 2 using Python: integration, intuition, code
SECTION: Improper integrals
LECTURE: Two infinite bounds
"""
import numpy as np
import sympy as sym
import matplotlib.pyplot as plt

# define the function
x = sym.symbols('x')
fx = 4*x / (x**4+2)

# sympy plot
sym.plot(fx, (x, -10, 10))

# print the indefinite integral

# definite integrals from each side, and total
print('')
                                     sym.latex(sym.integrate(fx, (x, 0, sym.oo)).evalf()))))
print('')

