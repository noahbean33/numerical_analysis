"""CodeChallenge: Infinite functions to sketch

COURSE: Master calculus 1 using Python: derivatives and applications
SECTION: Functions
LECTURE: CodeChallenge: Infinite functions to sketch
"""
import numpy as np
import sympy as sym
import matplotlib.pyplot as plt

from IPython.display import Math

# Exercise 1: Polynomials

# random polynomial coefficients
x = np.linspace(-3, 3, 101)
coefs = np.random.randint(-5, 6, 3)

# the function
fx = coefs[0] + coefs[1]*x + coefs[2]*x**2

# print the function to sketch
print(f'Sketch this!\ny = {coefs[0]} + {coefs[1]}x + {coefs[2]}x**2')

### now to plot the figure

# the figure
plt.figure(figsize=(6, 6))

# the function
plt.plot(x, fx, linewidth=2)

# some key points
xpnts = [-1, 0, 1]
markers = [ 'ro', 'gs', 'mp' ]
for xi, mi in zip(xpnts, markers):
  y = coefs[0] + coefs[1]*xi + coefs[2]*xi**2
  plt.plot(xi, y, mi, label=f'when x={xi}')

# make it look nicer
plt.grid(color=[.8, .8, .8], linestyle='--')
plt.plot(x[[0, -1]], [0, 0], 'k', linewidth=2)
plt.plot([0, 0], plt.gca().get_ylim(), 'k', linewidth=2)
plt.legend()
plt.title(f'$y = {coefs[0]} + {coefs[1]}x + {coefs[2]}x^2$')
plt.show()

# Exercise 2: e and cos using sympy

# hard-coded exponential and cos

t = sym.var('theta')

# random integer coefficients, excluding zero
coefs = np.random.choice([i for i in range(-3, 4) if i!=0])

sfx = coefs*sym.exp(-t) * sym.cos(2*sym.pi*t)

print('Sketch this function!')
Math('f(\\theta) = ' + sym.latex(sfx))

# the figure
plt.figure(figsize=(6, 6))

# the function
y = sym.lambdify(t, sfx)
plt.plot(x, y(x), linewidth=2)

# one key point
plt.plot(0, y(0), 'ro', label='when x=0')

# make it look nicer
plt.grid(color=[.8, .8, .8], linestyle='--')
plt.plot(x[[0, -1]], [0, 0], 'k', linewidth=2)
plt.plot([0, 0], plt.gca().get_ylim(), 'k', linewidth=2)
plt.legend()
plt.show()

# Exercise 3: random piecewise function

negativeX = [ 'x', 'x**2', 'x**3'  ]
positiveX = [ 'np.log', 'np.sqrt' ]

# x-axis grid to evaluate on
x = np.linspace(-3, 3, 101)

# random function choice
randFunIdx = [ np.random.choice(np.arange(len(negativeX))), 
               np.random.choice(np.arange(len(positiveX))) ]

# define negative side of function
fx = eval( negativeX[randFunIdx[0]] )

# define positive side of function
fx[x>0] = eval( positiveX[randFunIdx[1]] + '(x[x>0])' )

# print out function name
print('Sketch this!!\n')
print(f'{negativeX[randFunIdx[0]]} for x<=0')
print(f'{positiveX[randFunIdx[1]][3:]}(x) for x>0')

# and plot the function
plt.plot(x[x<=0], fx[x<=0], linewidth=2, label=negativeX[randFunIdx[0]])
plt.plot(x[x>0], fx[x>0], linewidth=2, label=positiveX[randFunIdx[1]][3:])
plt.plot(x[[0, -1]], [0, 0], '--', color=[.4, .4, .4], linewidth=.4)
plt.plot([0, 0], [-5, 5], '--', color=[.4, .4, .4], linewidth=.4)
plt.xlim(x[[0, -1]])
plt.ylim([-5, 5])
plt.legend()
plt.show()

