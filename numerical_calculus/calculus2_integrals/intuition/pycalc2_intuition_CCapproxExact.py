"""CodeChallenge: Approximate exact integrals

COURSE: Master calculus 2 using Python: integration and applications
SECTION: Intuition for integration
LECTURE: CodeChallenge: Approximate exact integrals
"""
import numpy as np
import sympy as sym
import matplotlib.pyplot as plt

# Exercise 1: Algebraic approximations of indefinite integrals

# a python function to approximate an integral using computational methods
def numericalIntegral(x, fx):

  # find the x-axis coordinate of x=0
  zeroIdx = np.argmin(abs(x-0))

  # cumulative sum (discrete integral)
  dx = x[1] - x[0]
  idf = np.cumsum(fx) * dx
  idf -= idf[zeroIdx] # normalize so that idf(0)=0
  idf += fx[zeroIdx]  # then add constant from original function

  return idf

# create a symbolic function and gets its analytical integral
from sympy.abc import x

# the function and its integral
fx_s = sym.sin(x) * x**3
intf_s = sym.integrate(fx_s, x)

# print the function and its antiderivative

# lambidfy both functions
fx_l = sym.lambdify(x, fx_s)
intf_l = sym.lambdify(x, intf_s)

# get its computational (empirical) integral
xx = np.linspace(-np.pi, np.pi, 31)
intf_c = numericalIntegral(xx, fx_l(xx))

# plot for comparison
plt.plot(xx, intf_c, 'ms', label='Numerical (numpy)')
plt.plot(xx, intf_l(xx), 'k', label='Analytical (sympy)')

plt.legend()
plt.xlabel('x')
plt.ylabel(r'$\int f(x) dx$')
plt.xlim(xx[[0, -1]])
plt.show()

# Exercise 2: Approximation error for different $\Delta$x

# compute RMS for different [\Delta x]'s
deltaXs = np.logspace(np.log10(.5), np.log10(.001), 20)
RMSs = np.zeros(len(deltaXs))

for i, dx in enumerate(deltaXs):

  # compute empirical integral
  xx = np.arange(-np.pi, np.pi+dx, dx)
  intf_a = numericalIntegral(xx, fx_l(xx))

  # compute approximation error as root-mean-squared error
  RMSs[i] = np.mean((intf_l(xx) - intf_a)**2)**(1/2)

# visualize the error
_, ax = plt.subplots(1, figsize=(10, 6))
ax.plot(deltaXs, RMSs, 'ks-', linewidth=2, markerfacecolor='w', markersize=10)
ax.invert_xaxis()
ax.axhline(0, linestyle='--', color='m')

ax.set(xlabel=r'$\Delta x$', ylabel='Approximation error (a.u.)')
ax.set_xscale('log')
# ax.set_yscale('log')
ax.legend(['Approximations', 'True integral'])
plt.show()

# Exercise 3: Geometric approximation of definite integrals

# function bounds
bounds = [-1, 2]

# create a definite integral object for display
expr = sym.Integral(fx_s, (x, bounds)) # doesn't actually integrate

# compute the analytic definite integral
defIntegral = sym.integrate(fx_s, (x, bounds[0], bounds[1])) # note list unpacking in the previous line

# print the symbol and numerical result
Math('%s \;=\; %s \;\\approx\; %s' %(sym.latex(expr), sym.latex(defIntegral), sym.N(defIntegral)))

# resolutions
areas = np.zeros(len(deltaXs))

# loop over resolutions
for i, dx in enumerate(deltaXs):
  xx = np.arange(bounds[0], bounds[1]+dx, dx)

  # compute and store area (using list comprehension here)
  areas[i] = np.sum([ fx_l(xi)*dx for xi in xx ])

# create an axis object (easier to invert the axis...)
_, ax = plt.subplots(1, figsize=(10, 5))

# plot the results
ax.plot(deltaXs, areas, 'ks-', linewidth=2, markerfacecolor='w', markersize=10, label='Empirical estimate')
ax.axhline(defIntegral, linestyle='--', color='m', label='True integral')

ax.legend()
ax.invert_xaxis()
ax.set_xscale('log')
ax.set(xlabel=r'$\Delta x$', ylabel='Area (estimate of definite integral)')
plt.show()

