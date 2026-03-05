"""CodeChallenge: Derivatives of derivatives...

COURSE: Master calculus 1 using Python: derivatives and applications
SECTION: Differentiation rules and theorems
LECTURE: CodeChallenge: Derivatives of derivatives...
"""
import numpy as np
import sympy as sym
import matplotlib.pyplot as plt

from IPython.display import display

# Exercise 1: Third derivatives in numpy

# define the x-axis grid
dx = .01
x = np.arange(-np.pi, np.pi, dx)

# define the function
f = .1*x**4 + np.exp(-x**2) + np.cos(x)

# compute the derivatives
df = np.diff(f) / dx
ddf = np.diff(df) / dx
dddf = np.diff(ddf) / dx

# plot!

# setup the figure and define the titles
_, axs = plt.subplots(4, 1, figsize=(4, 10))
titles = [ "f(x)", "f'(x)", "f''(x)", "$f^{(3)}(x)$" ]

# plot the lines
axs[0].plot(x, f)
axs[1].plot(x[:-1], df)
axs[2].plot(x[:-2], ddf)
axs[3].plot(x[:-3], dddf)


# applies to all axes
for a, t in zip(axs, titles):
  a.set_xlim(x[[0, -1]])
  a.set_title(t)
  a.spines['right'].set_visible(False)
  a.spines['top'].set_visible(False)

plt.tight_layout()
plt.show()

# Exercise 2: Using np.diff second input

# specify the derivative order as the second input to np.diff
dfI = np.diff(f, 1) / dx
ddfI = np.diff(f, 2) / dx**2
dddfI = np.diff(f, 3) / dx**3

# test whether they're the same
print(f'Difference for first derivative:  {np.mean(np.abs(dfI-df))}')
print(f'Difference for second derivative: {np.mean(np.abs(ddfI-ddf))}')
print(f'Difference for third derivative:  {np.mean(np.abs(dddfI-dddf))}')

# Exercise 3: Higher-order derivatives in sympy

# define the function
x = sym.symbols('x')
sf = 3*x**4 + sym.exp(-x**2) + sym.cos(x)


print(f'The function is:')
display(sf), print()

# compute and show the derivatives
for i in range(1, 4):
  print(f'The {i}-order derivative is:')
  display(sym.diff(sf, x, i)) # try sym.simplify!
  print()

