"""CodeChallenge: Derivative of c^x and x^x

COURSE: Master calculus 1 using Python: derivatives and applications
SECTION: Differentiation rules and theorems
LECTURE: CodeChallenge: Derivative of c^x and x^x
"""
import numpy as np
import sympy as sym
import matplotlib.pyplot as plt

from IPython.display import display, Math

# Exercise 1: Differentiating 2^x

# create a symbolic variable
x = sym.symbols('x')

# define expression
fx = 2**x

# differentiate it!
df = sym.diff(fx, x)

# print out both
display(Math(f'f(x) = {sym.latex(fx)}'))
display(Math(f"f'(x) = {sym.latex(df)}"))

# lambdify
fx_lam = sym.lambdify(x, fx)
df_lam = sym.lambdify(x, df)

# create an x-grid
xx = np.linspace(-2, 3, 1001)

# plot!
plt.plot(xx, fx_lam(xx), label=f'$f(x) = {sym.latex(fx)}$', linewidth=2)
plt.plot(xx, df_lam(xx), label=f"$f'(x) = {sym.latex(df)}$", linewidth=2)
plt.plot(xx, np.exp(xx), label=f"$f'(x) = e^x$", linewidth=2)

plt.legend()
plt.xlabel('x')
plt.ylabel("f(x) or f'(x)")
plt.xlim(xx[[0, -1]])
plt.grid()
plt.show()

# Exercise 2: Differentiating x^x

# define expression
fx = x**x

# differentiate it!
df = sym.diff(fx, x)

# print out both
display(Math(f'f(x) = {sym.latex(fx)}'))
display(Math(f"f'(x) = {sym.latex(df)}"))

# lambdify
fx_lam = sym.lambdify(x, fx)
df_lam = sym.lambdify(x, df)

# create an x-grid
xx = np.linspace(-1, 2, 1001)

# plot!
plt.plot(xx, np.real(fx_lam(xx)), label=f'$f(x) = {sym.latex(fx)}$', linewidth=2)
plt.plot(xx, df_lam(xx), label=f"$f'(x) = {sym.latex(df)}$", linewidth=2)

plt.legend()
plt.xlabel('x')
plt.ylabel("f(x) or f'(x)")
plt.xlim(xx[[0, -1]])
plt.grid()
plt.show()

# just a bit of fun with (-c)**x

k = np.linspace(-1, -5, 100)
q = np.linspace(-np.pi/2, np.pi/2, 1000)

for i, ki in enumerate(k):
  z = np.power(ki, q, dtype=complex)
  plt.plot(np.real(z), np.imag(z), linewidth=.7, color=[.8*i/len(k), .7-.6*i/len(k), i/len(k)])

plt.axis('off')
plt.show()

