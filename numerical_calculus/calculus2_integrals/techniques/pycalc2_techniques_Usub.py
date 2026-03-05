"""U-substitution

COURSE: Master calculus 2 using Python: integration, intuition, code
SECTION: Integration techniques
LECTURE: U-substitution
"""
import numpy as np
import sympy as sym
import matplotlib.pyplot as plt

x, C = sym.symbols('x, C')

# define the function and its antiderivative
fx = x / (x**2 + 2)
# fx = (3*x**4+5)**6 * x**3

antideriv = sym.integrate(fx)

# show the result using latex

# the actual latex code
'%s = %s+C' %(sym.latex(sym.Integral(fx)), sym.latex(antideriv))

# and visualize the function
xx = np.linspace(-2, 5, 351) # x-axis grid
y = [fx.subs(x, xi) for xi in xx] # function
F = [antideriv.subs(x, xi) for xi in xx] # indefinite integral

# plotting
_, axs = plt.subplots(1, figsize=(10, 5))

axs.plot(xx, y, linewidth=2, label=r'f(x) = $%s$'%sym.latex(fx))
axs.plot(xx, F, linewidth=2, label=r'F(x) = $%s+0$'%sym.latex(antideriv))
axs.axhline(0, linestyle='--', color=[.8, .8, .8], zorder=-3)

axs.set(xlim=xx[[0, -1]], xlabel='x', ylabel='f(x) or F(x)')
axs.legend()
plt.show()

# test whether my answer matches sympy's
myAns = (3*x**4+5)**7/84
sym.expand(myAns)# == antideriv

