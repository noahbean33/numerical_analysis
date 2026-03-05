"""CodeChallenge: Math in Python

COURSE: Master calculus 1 using Python: derivatives and applications
SECTION: Functions
LECTURE: CodeChallenge: Math in Python
"""
import numpy as np
import sympy as sym
import matplotlib.pyplot as plt

# Exercise 1: function in numpy

### in numpy

# domain for x
xDomain = [ -2, 2 ]

# grid resolution ("step" parameter)
resolution = .1

# create grid of x-axis values
x = np.arange(xDomain[0], xDomain[1]+resolution, resolution)

# Or:
numSteps = 41
x = np.linspace(xDomain[0], xDomain[1], numSteps)

# function
y = x**2 + 3*x**3 - x**4


# and plot
plt.figure(figsize=(8, 6))
plt.plot(x, y, linewidth=2, label='$y=x^2 + 3x^3 - x^4$')
plt.legend()
plt.grid()
plt.xlim([x[0], x[-1]])
plt.ylim([np.min(y), np.max(y)])
plt.xlabel('x')
plt.ylabel('y=f(x)')
plt.show()

# Exercise 2: in sympy

# create a symbolic variable
s_beta = sym.var('beta')

# define the function
s_y = s_beta**2 + 3*s_beta**3 - s_beta**4

# use sympy's plotting engine
sym.plot(s_y, (s_beta, xDomain[0], xDomain[1]), axis_center='auto',
         title=f'$f(\\beta) = {sym.latex(s_y)}$',
         xlabel='x', ylabel=None)#'$y=f(\\beta)$')

plt.show()

# Exercise 3: convert sympy to numpy

##

# create the function object
fx = sym.lambdify(s_beta, s_y)

# evaluate one x-axis value
fx(2)

# get a list of values in numpy and plot with matplotlib

yy = fx(x)


# and plot
plt.figure(figsize=(8, 6))
plt.plot(x, yy, linewidth=2, label='$y=x^2 + 3x^3 - x^4$')
plt.legend()
plt.grid()
plt.xlim([x[0], x[-1]])
plt.ylim([np.min(yy), np.max(yy)])
plt.xlabel('x')
plt.ylabel('y=f(x)')
plt.show()

