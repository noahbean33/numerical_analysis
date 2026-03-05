"""CodeChallenge: Numerical approximations

COURSE: Master calculus 2 using Python: integration, intuition, code
SECTION: Applications in geometry
LECTURE: CodeChallenge: Numerical approximations
"""
import numpy as np
import sympy as sym
import matplotlib.pyplot as plt
import scipy.integrate as spi

# Exercise 1: Initial exploration in sympy

# variable, function, integral
x = sym.symbols('x')

fx = sym.log(x)
gx = sym.integrate(fx)

sym.plot(fx, gx, (x, .001, 4.5), ylim=[-1.5, 2])

# find the intersection points
sym.solve(fx-gx)

# Exercise 2: Transform to numpy and visualize

# lambdify the functions
fx_l = sym.lambdify(x, fx)
gx_l = sym.lambdify(x, gx)
diff_l = sym.lambdify(x, fx-gx) # used in exercise 4

# evaluate the functions
xx = np.linspace(.01, 4.5, 123)

# and draw
plt.figure(figsize=(8, 6))
plt.plot(xx, fx_l(xx), linewidth=2, label=r'$f(x) = %s$' %sym.latex(fx))
plt.plot(xx, gx_l(xx), linewidth=2, label=r'$g(x) = %s$' %sym.latex(gx))

plt.gca().set(xlabel='x', ylabel='y', xlim=xx[[0, -1]], ylim=[-1.5, 2])
plt.legend()
plt.show()

# Exercise 3: Approximate function intersections

# function difference
fun_diff = np.abs(fx_l(xx)-gx_l(xx))

plt.plot(xx, fun_diff)
plt.ylim(0, 1.5)
plt.xlabel('x')
plt.ylabel('|f-g|')
plt.show()

# find points closest to zero
from scipy.signal import find_peaks

peekz = find_peaks(-fun_diff)[0]
intersection_points = xx[peekz]

print(intersection_points)

# and draw
plt.figure(figsize=(8, 6))
plt.plot(xx, fx_l(xx), linewidth=2, label=r'$f(x) = %s$' %sym.latex(fx))
plt.plot(xx, gx_l(xx), linewidth=2, label=r'$g(x) = %s$' %sym.latex(gx))

x4area = np.linspace(intersection_points[0], intersection_points[1], 79)
plt.fill_between(x4area, fx_l(x4area), gx_l(x4area), color='k', alpha=.5)

plt.plot(intersection_points, fx_l(intersection_points), 'ko', markersize=10, markerfacecolor='w')

plt.gca().set(xlabel='x', ylabel='y', xlim=xx[[0, -1]], ylim=[-1.5, 2])
plt.legend()
plt.show()

# Exercise 4: Numerical approximation using scipy

# empirical areas
fx_int, _ = spi.quad(fx_l, intersection_points[0], intersection_points[1])
gx_int, _ = spi.quad(gx_l, intersection_points[0], intersection_points[1])
diff_int, _ = spi.quad(diff_l, intersection_points[0], intersection_points[1])

print('')
print('')

