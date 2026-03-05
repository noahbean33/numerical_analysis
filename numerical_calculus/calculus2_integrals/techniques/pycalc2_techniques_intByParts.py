"""Integration by parts

COURSE: Master calculus 2 using Python: integration, intuition, code
SECTION: Integration techniques
LECTURE: Integration by parts
"""
import numpy as np
import sympy as sym
import matplotlib.pyplot as plt

x, C = sym.symbols('x, C')

fx = x*sym.cos(x)
# fx = sym.exp(-x*sym.pi)*sym.sin(7*x)
antideriv = sym.integrate(fx)

# show the result using latex

# discretize the function
xx = np.linspace(-2*np.pi, 3*np.pi, 403)
y = [fx.subs(x, xi) for xi in xx]
F = [antideriv.subs(x, xi) for xi in xx]

# and make some lovely plots :)
_, axs = plt.subplots(1, 2, figsize=(12, 5))

axs[0].plot(xx, y, label='f')
axs[0].plot(xx, F, label='F')
axs[0].set(xlim=xx[[0, -1]], xlabel='x', ylabel='y=f(x) or F(x)')
axs[0].legend()

axs[1].plot(y, F, 'k', linewidth=2)
axs[1].set(xlabel='f(x)', ylabel='F(x)')

plt.tight_layout()
plt.show()

