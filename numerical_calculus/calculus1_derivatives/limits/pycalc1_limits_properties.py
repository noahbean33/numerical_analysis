"""CodeChallenge: properties of limits

COURSE: Master calculus 1 using Python: derivatives and applications
SECTION: Limits
LECTURE: CodeChallenge: properties of limits
"""
import numpy as np
import sympy as sym
import matplotlib.pyplot as plt

# Exercise 1: lim(c*f) = c*lim(f)

# a function in sympy
from sympy.abc import x

# define the function and plot
fx = x**3/3 + 100*sym.sqrt(sym.Abs(x))
sym.plot(fx, (x, -10, 10), ylim=[-100, 500])fx

# demonstrate the constant-factor property
c = np.random.randn()
print('   lim(c*fx):')
print( sym.N(sym.limit(c*fx, x, 5)) )

print(' ')
print('   c*lim(fx):')
print( sym.N(c*sym.limit(fx, x, 5)) )

# Exercise 2: lim(f+g) = lim(f) + lim(g)

f = sym.log(x) + x**2
g = sym.exp(-x) + x**3

print( sym.limit(f+g, x, np.pi) )
print( sym.limit(f, x, np.pi)+sym.limit(g, x, np.pi) )

# use sym.pi or np.pi?
sym.limit(f+g, x, sym.pi)

# Exercise 3: lim(f*g) = lim(f)lim(g)

# use the same functions as above
print( sym.limit( f*g , x, np.pi) )
print( sym.limit(f, x, np.pi)*sym.limit(g, x, np.pi) )

# also for powers
print( sym.limit(f**3, x, np.pi) )
print( sym.limit(f, x, np.pi)*sym.limit(f, x, np.pi)*sym.limit(f, x, np.pi) )

# Exercise 4: lim(f/g) = lim(f)/lim(g)

# use the same functions as above
print( sym.limit( f/g , x, np.pi) )
print( sym.limit(f, x, np.pi)/sym.limit(g, x, np.pi) )

# but be mindful of ?/0
h = x**3 + x**2 + x

print( sym.limit( g, x, 0) )
print( sym.limit( h, x, 0) )
print( sym.limit( g/h , x, 0) )

# it's still a valid function
g/h

# FYI: sym.factor(g/h)

