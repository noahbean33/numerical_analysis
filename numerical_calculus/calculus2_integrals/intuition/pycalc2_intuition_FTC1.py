"""The fundamental theorem of calculus, Part 1

COURSE: Master calculus 2 using Python: integration and applications
SECTION: Intuition for integration
LECTURE: The fundamental theorem of calculus, Part 1
"""
import numpy as np
import sympy as sym
import matplotlib.pyplot as plt

# # FTC1: the integral of a derivative is the function

# create symbolic variables
x, C = sym.symbols('x, C')

# create a function
fx = (x-1)**2

# take its derivative
df = sym.diff(fx, x)

# integrate the derivative
id = sym.integrate(df, x) + C

# print the results

# show that F(f(x)')==f(x) with the constant

# # Visualize the functions

# quick-n-dirty plotting
sym.plot(fx)
sym.plot(id.subs(C, 1))

# plotting with matplotlib

# lambdify all functions
fx_l = sym.lambdify(x, fx)
df_l = sym.lambdify(x, df)
id_l = sym.lambdify(x, id.subs(C, 0)) # experiment with C!

# define x-axis grid
xx = np.linspace(-1, 4, 23)

# and plot
plt.figure(figsize=(10, 7))
plt.plot(xx, fx_l(xx), 'k', label='f(x)')
plt.plot(xx, df_l(xx), 'rd', label="f'(x)")
plt.plot(xx, id_l(xx), 'bo', markersize=8, label="F(f'(x))")

plt.gca().set(xlim=xx[[0, -1]], xlabel='x', ylabel='y or dy/dx')
plt.legend()
plt.grid()
plt.show()

