"""Functions with discontinuities

COURSE: Master calculus 2 using Python: integration, intuition, code
SECTION: Improper integrals
LECTURE: Functions with discontinuities
"""
import numpy as np
import sympy as sym
import matplotlib.pyplot as plt

# # Jump discontinuities

x = sym.symbols('x')

fx = sym.Piecewise((x/2, x<0), (x**2+1, x>=0))
a, b = -2, 1

sym.plot(fx, (x, a-1, b+1))
sym.integrate(fx, (x, a, b))

# # Infinite discontinuity

fx = 1 / sym.sqrt(x-1)
a, b = 1, 2

sym.plot(fx, (x, a-1, b+1), ylim=[0, 10])
sym.integrate(fx, (x, a, b))

# # Removable discontinuity

fx = (x**2-2*x) / (x**2-4)
a, b = 0, 4

sym.plot(fx, (x, a-1, b+1), ylim=[-1, 1])
sym.integrate(fx, (x, a, b)).evalf()

