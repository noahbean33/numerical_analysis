"""Curve (arc) length: practice (Python)

COURSE: Master calculus 2 using Python: integration, intuition, code
SECTION: Applications in geometry
LECTURE: Curve (arc) length: practice (Python)
"""
import numpy as np
import sympy as sym
import scipy.integrate as spi
import matplotlib.pyplot as plt

# # Attempts in sympy

# parametric variable
t = sym.symbols('t')

# the two functions
xt = sym.cos(2*t)
yt = sym.sin(t**2)

# sympy plot
sym.plot_parametric(xt, yt, (t, 0, sym.pi))

C = sym.Curve((xt, yt) , (t, 0, sym.pi))
# C.length # sympy can't calculate it

# functions and their derivatives
xt  = sym.cos(2*t)
dxt = sym.diff(xt)

yt  = sym.sin(t**2)
dyt = sym.diff(yt)

# the integrand
integrand = sym.sqrt( dxt**2 + dyt**2 )

# print the intermediate reults

# antiderivative (sympy crashed Python after running out of RAM. lol)
# antideriv = sym.integrate(integrand)

# # Now for numpy

# curve length in numpy
t = np.linspace(0, np.pi, 123)
x = np.cos(2*t)
y = np.sin(t**2)

colors = np.linspace([0, .2, .5], [.8, .5, 1], len(t))

segLengths = np.zeros(len(t))

for i in range(1, len(t)):

  # calculate deltas
  dx = x[i] - x[i-1]
  dy = y[i] - y[i-1]

  # this little curve segment
  segLengths[i] = np.sqrt( dx**2 + dy**2 )

# version without for-loops
dx = x[1:] - x[:-1]
dy = y[1:] - y[:-1]
segLengths = np.append(0, np.sqrt( dx**2 + dy**2 ))

# plot
_, axs = plt.subplots(1, 3, figsize=(12, 3.5))
axs[0].scatter(x, y, s=20, c=colors)
axs[0].set(xlabel='x', ylabel='y', title=r'$\bf{A}$)  The curve')

for ti in np.linspace(len(t)*.2, len(t)*.95, 4, dtype=int):
  axs[0].annotate(f't={t[ti]:.1f}', [x[ti], y[ti]])
  axs[1].axvline(t[ti], linestyle=':', color=colors[ti, :], zorder=-4)
  axs[2].axvline(t[ti], linestyle=':', color=colors[ti, :], zorder=-4)

axs[1].scatter(t, segLengths, s=20, c=colors)
axs[1].set(xlabel='t', ylabel='length (a.u.)', title=r'$\bf{B}$)  Segment lengths')

axs[2].scatter(t, np.cumsum(segLengths), s=20, c=colors)
axs[2].set(xlabel='t', ylabel='length (a.u.)', title=r'$\bf{C}$)  Cumulative lengths')

print(f'Total curve length for n = {len(t)}: {np.sum(segLengths)}')

plt.tight_layout()
plt.show()

# # Using spi.simpson

# Parameter values for the interval
a = 0
b = np.pi
t = np.linspace(a, b, 500)

# Calculate derivatives empirically
dx_dt = np.gradient( np.cos(2*t) , t)
dy_dt = np.gradient( np.sin(t**2), t)

# Use Simpson's rule to integrate
integrand = np.sqrt(dx_dt**2 + dy_dt**2)
L = spi.simpson(integrand, x=t)

print(f'Arc length spi.simpson: {L}')
print(f'Arc length using numpy: {np.sum(segLengths)}')

# # Using spi.quad

p  = sym.symbols('p')

# the functions
xp = sym.cos(2*p)
yp = sym.sin(p**2)

# their derivatives
dxp = sym.diff(xp)
dyp = sym.diff(yp)

# the integrand
integrand = sym.lambdify(p, sym.sqrt(dxp**2 + dyp**2) )

# and now to integrate
a = 0
b = np.pi
L, _ = spi.quad(integrand, a, b)

print(f'Arc length using spi.quad: {L}')

