"""CodeChallenge: Complete partial differentiation exercises

COURSE: Master calculus 1 using Python: derivatives and applications
SECTION: Multivariable differentiation
LECTURE: CodeChallenge: Complete partial differentiation exercises
"""
import numpy as np
import sympy as sym
import matplotlib.pyplot as plt

# latex display functions
from IPython.display import display, Math

# Exercise 1: The exercise-spawning exercise

# create variables x and y
x, y = sym.symbols('x, y')

# random polynomial coefficient and order
randCoefsX = np.random.choice((-5, -4, -3, -2, -1, 1, 2, 3, 4, 5), 2)
randCoefsY = np.random.choice((-5, -4, -3, -2, -1, 1, 2, 3, 4, 5), 2)

# list of functions to sample from
funListX = [ sym.cos(x), sym.sin(x), sym.log(x), sym.exp(x), randCoefsX[0]*x**randCoefsX[1] ]
funListY = [ sym.cos(y), sym.sin(y), sym.log(y), sym.exp(y), randCoefsY[0]*y**randCoefsY[1] ]

# create the practice problem by selecting two terms to multiply
funsX  = np.random.choice(funListX, 2, replace=False)
funsY  = np.random.choice(funListY, 2, replace=False)
funsXY = np.random.choice(funListX, 1)
fxy = funsX[0]*funsY[0] + funsX[1]*funsY[1] + funsXY[0].subs(x, x*y)

# print the function
display(Math('f(x, y) = %s' %sym.latex(fxy)))
display(Math('f_x = ?'))
display(Math('f_y = ?'))

# print the partial derivatives
display(Math('f_x = %s' %sym.latex(sym.diff(fxy, x))))
print(' ')

display(Math('f_y = %s' %sym.latex(sym.diff(fxy, y))))

