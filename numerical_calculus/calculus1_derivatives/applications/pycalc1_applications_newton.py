"""Newton's method for finding roots of functions.

COURSE: Master calculus 1 using Python: derivatives and applications
SECTION: Applications
LECTURE: Newton's roots
TEACHER: Mike X Cohen, sincxpress.com
"""
import numpy as np
import sympy as sym
import matplotlib.pyplot as plt


# Exercise 1: Roots of a sympy expression
from sympy.abc import x

# define the function
fx = 2*x**3 - 3

# find the real root
realRoot = sym.N(sym.solve(fx, x)[0])
realRoot


# Exercise 2: Implement Newton's method

def newtonIter(f, d, x0):
    """Perform one iteration of Newton's method.
    
    Args:
        f: Function (sympy expression)
        d: Derivative of function (sympy expression)
        x0: Current estimate of root
        
    Returns:
        Updated estimate of root
    """
    return x0 - f.subs(x, x0) / d.subs(x, x0)

# function derivative
df = sym.diff(fx)

# start value (aka x0)
start = 1
x1 = newtonIter(fx, df, start)
print(f'Estimate of root from first iteration: {x1}')

# a second iteration
x2 = newtonIter(fx, df, x1)
print(f'Estimate of root from second iteration: {x2}')


# Exercise 3: Iterations in a loop
# multiple iterations in a loop
numIters = 7

# initialize x0 and vector of all guesses
startGuess = 1
xGuess = np.zeros(numIters) + startGuess
# xGuess = np.full(numIters, startGuess, dtype=np.float64) # equivalent to previous

# loop over iterations
for i in range(1, numIters):
  xGuess[i] = newtonIter(fx, df, xGuess[i-1])

# plot the guesses
plt.plot(xGuess, 's-')
plt.plot([0, numIters-1], [realRoot, realRoot], 'r--', label='True root')
plt.xlabel('Iteration')
plt.ylabel('Root approximation')
plt.legend()
plt.show()

# plot the function and its root-approximations

# lambdify the function
fx_fun = sym.lambdify(x, fx)
xx = np.linspace(-1, 2, 301)

# plot the function and true root
plt.plot(xx[[0, -1]], [0, 0], '--', color=[.7, .7, .7])
plt.plot(xx, fx_fun(xx), linewidth=2, label='f(x)')
plt.xlim(xx[[0, -1]])
plt.ylim([-10, 10])
plt.plot([realRoot, realRoot], plt.gca().get_ylim(), '--', color=[1, .6, .6], label='True root')

# (optional) change red intensity for each update
redvals = np.linspace(.2, 1, len(xGuess))

# plot in a loop (can do without the loop with static color)
for g, r in zip(xGuess, redvals):
  plt.plot(g, fx_fun(g), 'o', markersize=8, color=[r, .1, .3])

# finalize the plot
# plt.xlim([np.min(xGuess)*.9, np.max(xGuess)*1.1])
plt.legend()
plt.show()


# Exercise 4: Start further away
# To test, change variable 'startGuess' to -5


# Exercise 5: A different function
# define the function and its derivative
fx = sym.cos(x) - x**2
df = sym.diff(fx)

# find the roots using sympy
sym.solve(fx, x)


# plot it to see that there are roots
sym.plot(fx, (x, -2, 2))


# multiple iterations in a loop
numIters = 7

# initialize x0 and vector of all guesses
startGuess = 1
xGuess = np.zeros(numIters) + startGuess

# loop over iterations
for i in range(1, numIters):
  xGuess[i] = newtonIter(fx, df, xGuess[i-1])

# plot the guesses
plt.plot(xGuess, 's-')
plt.show()

# plot the function and its root-approximations

# lambdify the function
fx_fun = sym.lambdify(x, fx)
xx = np.linspace(-1.5, 1.5, 301)

# plot the function and true root
plt.plot(xx[[0, -1]], [0, 0], '--', color=[.7, .7, .7])
plt.plot(xx, fx_fun(xx), linewidth=2, label='f(x)')
plt.xlim(xx[[0, -1]])
plt.ylim([-1, .5])

# (optional) change red intensity for each update
redvals = np.linspace(.2, 1, len(xGuess))

# plot in a loop (can do without the loop with static color)
for g, r in zip(xGuess, redvals):
  plt.plot(g, fx_fun(g), 'o', markersize=8, color=[r, .1, .3])

# finalize the plot
# plt.xlim([np.min(xGuess)*.9, np.max(xGuess)*1.1])
plt.show()
