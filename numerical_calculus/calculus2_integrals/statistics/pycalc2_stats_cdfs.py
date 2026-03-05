"""Cumulative distribution functions (cdfs)

COURSE: Master calculus 2 using Python: integration, intuition, code
SECTION: Applications in statistics
LECTURE: Cumulative distribution functions (cdfs)
"""
import numpy as np
import sympy as sym
import matplotlib.pyplot as plt
from scipy import stats
import sympy.stats

# # Creating a cdf in sympy

# define some variables and parameters
x = sym.symbols('x')
m = 1.5
alpha = 2
xx = np.linspace(.01, 5, 500)

# a sympy expression for the distribution
P = sym.stats.Pareto('P', m, alpha)
Pcdf_expr = sym.stats.cdf(P)(x)

# lambdify that
Pcdf_l = sym.lambdify(x, Pcdf_expr)

# numerically evaluate the cdf
cdf = Pcdf_l(xx)

# and plot
plt.figure(figsize=(8, 4))
plt.plot(xx, cdf)

# finalize the plot
plt.gca().set(xlim=xx[[0, -1]], xlabel='x', ylabel='Probability',
              title=f'Pareto cdf (m = {m}, $\\alpha$ = {alpha})')
plt.tight_layout()
plt.show()

# let's look at some values

# # Using scipy

# parameters
mu = 1
sigma = .3

# get the pdf values
xx = np.linspace(-5, 5, 401)
cdf = stats.logistic.cdf(xx, loc=mu, scale=sigma)

# and plot
plt.figure(figsize=(8, 3))
plt.plot(xx, cdf)
plt.axvline(mu, linewidth=1, color='gray', linestyle='--')

# finalize
plt.gca().set(xlim=xx[[0, -1]], xlabel='x', ylabel='Cumulative prob.', title=r'Logistic cdf ($\mu = %g, \sigma = %g$)' %(mu, sigma))
plt.tight_layout()
plt.show()

