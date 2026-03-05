"""CodeChallenge: Limits at discontinuities

COURSE: Master calculus 1 using Python: derivatives and applications
SECTION: Limits
LECTURE: CodeChallenge: Limits at discontinuities
"""
import numpy as np
import sympy as sym
import matplotlib.pyplot as plt

# Exercise 1: Jump discontinuity in numpy

# piecewise function

def fx(x):
  x = np.array(x)
  y = np.zeros(x.shape)

  tol = 10e-4
  y[x<-tol] = np.sin(x[x<-tol]*np.pi)
  y[x>tol] = -(x[x>tol]-2)**2
  y[np.abs(x)<tol] = 1.5
  return y


xx = np.linspace(-1, 2, 10001)
plt.plot(xx, fx(xx), 'o')
plt.xlabel('x')
plt.ylabel('y=f(x)')
plt.title('A function with a jump discontinuity')
plt.show()

# limit as x approaches 0 from the left

# x-axis coordinates getting closer to 0
xFromLeft  = -np.logspace(np.log10(.1), np.log10(.002), 10)
xFromRight =  np.logspace(np.log10(.002), np.log10(.1), 10)

# function values
limitFromLeft  = fx(xFromLeft)
limitFromRight = fx(xFromRight)

print(f'Limit approaches {limitFromLeft[-1]} from the left.')
print(f'Limit approaches {limitFromRight[0]} from the right.')
print(f'Function value at x=0:  {fx(0)}.')


# plot
plt.plot(xFromLeft, limitFromLeft, 's', label='From the left')
plt.plot(xFromRight, limitFromRight, 'o', label='From the right')
plt.plot(0, fx(0), 'rx', label='y=f(0)')
plt.legend()
plt.title(f'Function value at x=0 is {fx(0)}.')
plt.show()

# Exercise 2: Jump discontinuity in sympy

# "import" symbolic variable x
from sympy.abc import x

# list function pieces
piece1 = sym.sin(x*sym.pi)
piece2 = 1.5
piece3 = -(x-2)**2

# put them together with conditions
fx = sym.Piecewise( 
      (piece1, x<0),
      (piece2, sym.Eq(x, 0)),
      (piece3, x>0) 
      )


# plot
sym.plot(fx, (x, xx[0], xx[-1]))
plt.show()
fx

# test limits
print('Limit as x approaches 0 from the left:')
print( sym.N(sym.limit(fx, x, 0, dir='-')) )

print('\nLimit as x approaches 0 from the right:')
print( sym.limit(fx, x, 0, dir='+') )

print('\nTwo-sided limit as x approaches 0:')
print( sym.limit(fx, x, 0, dir='+-') )

print('\n\nFunction value at limit:')
print( sym.N(sym.limit(fx, x, 0)) )

# Exercise 3: Infinite discontinuity

fx = 3/(1-x**2)

sym.plot(fx, (x, -2, 2), ylim=[-10, 10])
plt.show()

# test limits
print('Limit as x approaches -1 from the left:')
print( sym.N(sym.limit(fx, x, -1, dir='-')) )

print('\nLimit as x approaches -1 from the right:')
print( sym.limit(fx, x, -1, dir='+') )

print('\nTwo-sided limit as x approaches -1:')
print( sym.limit(fx, x, -1, dir='+-') )

# Exercise 4: Oscillating discontinuity

fx = sym.sin(1/x)
sym.plot(fx, (x, -1, 1))
plt.show()

# test limits
print('Limit as x approaches 0 from the left:')
print( sym.N(sym.limit(fx, x, 0, dir='-')) )

print('\nLimit as x approaches 0 from the right:')
print( sym.limit(fx, x, 0, dir='+') )

print('\nTwo-sided limit as x approaches 0:')
print( sym.limit(fx, x, 0, dir='+-') )

