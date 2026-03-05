"""Area between two curves

COURSE: Master calculus 2 using Python: integration, intuition, code
SECTION: Applications in geometry
LECTURE: Area between two curves
"""
import numpy as np
import sympy as sym
import matplotlib.pyplot as plt

x = sym.symbols('x')

# the two functions
f1 = sym.sqrt(x)
f2 = x

# quick plot
sym.plot(f1, f2, (x, 0, 1.5))

# find the x-values where the functions intersect
intersection_points = sym.solve(f1-f2)

intersection_points

# find area between the two functions
area1 = sym.integrate(f1, (x, intersection_points[0], intersection_points[1]))
area2 = sym.integrate(f2, (x, intersection_points[0], intersection_points[1]))
areaBetween = sym.integrate(f1-f2, (x, intersection_points[0], intersection_points[1]))

print('')
print('')
                              sym.latex(sym.Integral(f2, (x, intersection_points[0], intersection_points[1]))),
                              area1-area2)))
print('')
                              areaBetween)))

# lambdify the functions
f1_l = sym.lambdify(x, f1)
f2_l = sym.lambdify(x, f2)

# evaluate the functions
xx = np.linspace(0, 1.5, 123)

x4area = np.linspace(float(intersection_points[0]), float(intersection_points[1]), 77)

# and draw
plt.figure(figsize=(8, 5))
plt.plot(xx, f1_l(xx), linewidth=2, label=r'$f_1(x) = %s$' %sym.latex(f1))
plt.plot(xx, f2_l(xx), linewidth=2, label=r'$f_2(x) = %s$' %sym.latex(f2))

plt.fill_between(x4area, f1_l(x4area), f2_l(x4area), color='k', alpha=.5)

plt.legend()
plt.show()

# the other example

f1 = sym.sin(x*10) + sym.log(x+.1) - (x-1)**2 + 3
f2 = x**2 + sym.cos(x*8)

# quick plot
sym.plot(f1, f2, (x, 0, 2))

# bounds
a = .5
b = 1.4

# definite integral using bounds from the slide
print('')
print('')

