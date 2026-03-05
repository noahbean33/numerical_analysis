"""CodeChallenge: approaching real infinity

COURSE: Master calculus 2 using Python: integration, intuition, code
SECTION: Improper integrals
LECTURE: CodeChallenge: approaching real infinity
"""
import numpy as np
import sympy as sym
import matplotlib.pyplot as plt
import scipy.integrate as spi

# matplotlib libraries for the colored lines
import matplotlib.cm as cm
import matplotlib.colors as mcolors

# # Exercise 1

from sympy.abc import x

# range of exponent values
pExponents = np.linspace(-3, -1.5, 21)

# x-axis grid values
xx = np.linspace(1, 10, 301)

# define the upper limit of integration (lower bound is hard-coded to 1)
upperLims = np.logspace(np.log10(2), np.log10(1e5), 43)
integrals = np.zeros(len(upperLims))

# define a colormap for the lines
fig, axs = plt.subplots(1, 2, figsize=(14, 4))
cmap = cm.rainbow
norm = mcolors.Normalize(vmin=pExponents.min(), vmax=pExponents.max())

# loop over exponents, calculate, plot
for p in pExponents:

  # create lambda function
  fx_l = sym.lambdify(x, x**p)

  # plot the function
  axs[0].plot(xx, fx_l(xx), color=cmap(norm(p)))

  # compute empirical integrals
  for ui in range(len(upperLims)):
    integrals[ui] = spi.quad(fx_l, 1, upperLims[ui])[0]

  # plot the the definite integral
  axs[1].plot(upperLims, integrals, color=cmap(norm(p)))

# add the colorbar
sm = cm.ScalarMappable(cmap=cmap, norm=norm)
cbar = plt.colorbar(sm, ax=axs[1])
cbar.set_label(r'Exponent (p in $x^p$)')

# make the plots look nicer
axs[0].set(xlim=xx[[0, -1]], xlabel='x', ylabel='y = f(x)', title='Function curves')
axs[1].set(xlim=upperLims[[0, -1]], xscale='log', xlabel='Upper bound',
           ylabel='Definite integral (A)', title=r'Area under $f(x)=x^p$')

plt.tight_layout()
plt.show()

