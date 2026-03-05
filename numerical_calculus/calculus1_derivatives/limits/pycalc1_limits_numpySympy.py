"""CodeChallenge: limits in numpy & sympy

COURSE: Master calculus 1 using Python: derivatives and applications
SECTION: Limits
LECTURE: CodeChallenge: limits in numpy & sympy
"""
import numpy as np
import sympy as sym
import matplotlib.pyplot as plt

# Exercise 1: Empirical limits in numpy

# a function for the function
def fx(u):
  return np.cos(u*np.pi) + np.log(u)**2

xx = np.linspace(.1, 2*np.pi, 201)

plt.plot(xx, fx(xx))
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid()
plt.show()

# limit as x approaches 3 from the left

# x-axis coordinates getting closer to 3
expFact = 4
g = 1.00001-np.linspace(1**expFact, .00001**expFact, 10)**(1/expFact)
xFromLeft = 3-g
xFromRight = 3+g


# function values
limitFromLeft  = fx(xFromLeft)
limitFromRight = fx(xFromRight)

print(f'Limit approaches {limitFromLeft[0]} from the left.')
print(f'Limit approaches {limitFromRight[0]} from the right.')
print(f'Function value:  {fx(3)} at x=3.')


plt.plot(xx, fx(xx), 'k', label='f(x)')
plt.plot(xFromLeft, limitFromLeft, 's', label='From the left')
plt.plot(xFromRight, limitFromRight, 'o', label='From the right')
plt.legend()
plt.title(f'Function value at x=3 is {fx(3)}.')
plt.xlim([2, 4])
plt.show()

# Exercise 2: Analytic limits in sympy

# create symbolic variable
from sympy.abc import x

# define function
sfx = sym.cos(x*sym.pi) + sym.log(x)**2

# function value at x=3
sfx.subs(x, 3)

print('Limit as x approaches 3 from the left:')
print( sym.limit(sfx, x, 3, dir='-') )

print('\nLimit as x approaches 3 from the right:')
print( sym.limit(sfx, x, 3, dir='+') )

print('\n\nFunction value at limit (sympy):')
print( sym.limit(sfx, x, 3, dir='+-') ) # optional sym.N()

print('\nFunction value at limit (numpy):')
print(fx(3))

# Exercise 3: Infinite limits

# create the functions as sympy expressions
fun2 = 1/( (x-2)**2 )

# convert to lambda object
fun2_numpy = sym.lambdify(x, fun2)

# plot using matplotlib
xx = np.linspace(0, 4, 1001) # why no warning with 1000?
plt.plot(xx, fun2_numpy(xx), linewidth=2)
plt.plot(xx[[0, -1]], [0, 0], '--', color=[.6, .6, .6])
plt.plot([2, 2], [0, 100], '--', color=[.6, .6, .6])
plt.ylim([0, 100])
plt.xlim(xx[[0, -1]])
plt.show()

print('Limit as x->2 from the left:  ' + str(sym.limit(fun2, x, 2, dir='-')))
print('Limit as x->2 from the right: ' + str(sym.limit(fun2, x, 2, dir='+')))
print('Limit as x->2 (two-sided):    ' + str(sym.limit(fun2, x, 2, dir='+-')))

# Exercise 4: Undefined limit

# create the function and visualize it
fun = sym.Abs(x-2)/(x-2)

sym.plot(fun, (x, -2, 4))

# limits
print('Limit as x->2 from the left : ' + str(sym.limit(fun, x, 2, dir='-')))
print('Limit as x->2 from the right: ' + str(sym.limit(fun, x, 2, dir='+')))
print('Two-sided limit as x->2: '      + str(sym.limit(fun, x, 2, dir='+-')))

# FYI, the limit object on its own
limitExp = sym.Limit(fun, x, 2)
limitExp#.doit()

