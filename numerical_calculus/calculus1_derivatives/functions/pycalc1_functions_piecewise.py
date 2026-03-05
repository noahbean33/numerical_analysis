"""CodeChallenge: Piecewise functions

COURSE: Master calculus 1 using Python: derivatives and applications
SECTION: Functions
LECTURE: CodeChallenge: Piecewise functions
"""
import numpy as np
import sympy as sym
import matplotlib.pyplot as plt

# Exercise 1: piecewise function in numpy

xx = np.linspace(-3, 5, 100)

# logic: function times boolean where the piece is true
piece1 =  0       * (xx<0)
piece2 = -2*xx    * ((xx>=0) & (xx<3))
piece3 = xx**3/10 * (xx>=3)

# stitch the pieces together
y = piece1 + piece2 + piece3


# and plot
plt.plot(xx, y, linewidth=2)
plt.xlabel('x')
plt.ylabel('y=f(x)')
plt.title('A piecewise function')
plt.show()

# Exercise 2: Draw separate lines

# plot the function pieces
plt.plot(xx[xx<0]             , np.zeros(np.sum(xx<0))  , linewidth=2, label='Piece 1')
plt.plot(xx[(xx>=0) & (xx<3)] , -2*xx[(xx>=0) & (xx<3)] , linewidth=2, label='Piece 2')
plt.plot(xx[xx>=3]            , xx[xx>3]**3/10          , linewidth=2, label='Piece 3')

# make the plot look a bit nicer
plt.legend()
plt.xlabel('x')
plt.ylabel('y=f(x)')
plt.title('A piecewise function')
plt.show()

# Exercise 3: piecewise function in sympy

# "import" symbolic variable x
from sympy.abc import x

# list function pieces
piece1 = 0
piece2 = -2*x
piece3 = x**3/10

# put them together with conditions
fx = sym.Piecewise( (piece1, x<0), (piece2, (x>=0) & (x<3)), (piece3, x>=3) )

# plot it
sym.plot(fx, (x, xx[0], xx[-1]), title='Piecewise function',
         xlabel='x', ylabel='y');

# Exercise 4: Evaluate the function at a point

# evaluate the function at a particular x-axis value
# e.g., find the value of the function at x=.5

# find that coordinate in xx
xloc = .5

# using numpy
xidx = np.argmin( (xx-xloc)**2 )
print(f'(numpy): At x={xx[xidx]:.5f}, f(x)={y[xidx]:.5f}')

# using sympy
print(f'(sympy): At x={xloc}, f(x)={fx.subs(x, xloc):.5f}')

