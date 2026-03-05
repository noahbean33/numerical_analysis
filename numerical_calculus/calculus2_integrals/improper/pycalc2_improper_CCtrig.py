"""CodeChallenge: Improper trig integrals

COURSE: Master calculus 2 using Python: integration, intuition, code
SECTION: Improper integrals
LECTURE: CodeChallenge: Improper trig integrals
"""
import numpy as np
import sympy as sym
import matplotlib.pyplot as plt
import scipy.integrate as spi

# Exercise 1: Improper trig integrals

x = sym.symbols('x')

# the function
fx = sym.cos(x)
# fx = sym.cos(x**2) # uncomment for exercise 2

# lambdify the function (twice to get net/total area)
fx_l_net = sym.lambdify(x, fx)
fx_l_tot = sym.lambdify(x, sym.Abs(fx))

# define the upper integration limits
upperLims = np.linspace(np.pi/4, 8*np.pi, 63)

# initialize the results vectors
defintNet = np.zeros(len(upperLims))
defintTot = np.zeros(len(upperLims))

# run the calculations!
for i, U in enumerate(upperLims):
  defintNet[i], _ = spi.quad(fx_l_net, 0, U)
  defintTot[i], _ = spi.quad(fx_l_tot, 0, U)

# plot the function
_, axs = plt.subplots(1, 2, figsize=(14, 4))
xx = np.linspace(0, upperLims[-1], 1001)
axs[0].plot(xx, fx_l_net(xx), linewidth=2)
axs[0].axhline(0, linestyle='--', color=[.7, .7, .7], zorder=-3)
axs[0].set(xlabel='Angle (x)', ylabel=r'$y = %s$'%sym.latex(fx),
           xlim=[0, upperLims[-1]], title='Function')

# and its integral as a function of upper bounds
axs[1].plot(upperLims, defintNet, label='Net area', linewidth=2)
axs[1].plot(upperLims, defintTot, label='Total area', linewidth=2)
axs[1].axhline(0, linestyle='--', color=[.7, .7, .7], zorder=-3)
axs[1].set(xlabel='Upper limit', ylabel='Area', xlim=upperLims[[0, -1]],
           title='Areas')
axs[1].legend()

plt.tight_layout()
plt.show()

# Exercise 3: Analytic integrals in sympy

# analytic improper integrals

fx = sym.Abs(sym.cos(x))
print('')

fx = sym.cos(x)
print('')

fx = sym.cos(x**2)

