"""CodeChallenge: Infinite limits exercises

COURSE: Master calculus 1 using Python: derivatives and applications
SECTION: Limits
LECTURE: CodeChallenge: Infinite limits exercises
"""
import numpy as np
import sympy as sym
import matplotlib.pyplot as plt

# Exercise 1: Factoring

# create symbolic variable
from sympy.abc import x

# random integer
a, b = np.random.randint(-4, 5, 2)

# random sign
c = np.random.choice((-1, 1))

# create the expression
expr = sym.expand( c*(x-a)*(x-b) ) / \
       sym.expand((x-a)*(x+b))


print(f'Compute the limit as x->{a} of:\n')
expr

# plot the function
sym.plot(expr, (x, -10, 10), ylim=[-10, 10])

# limits
print(f"Limit as x->{a} from the left : {sym.limit(expr, x, a, dir='-')}" )
print(f"Limit as x->{a} from the right: {sym.limit(expr, x, a, dir='+')}" )
print(f"Two-sided limit as x->{a}     : {sym.limit(expr, x, a, dir='+-')}" )
print(f"Function value at x={a}       : {expr.subs(x, a)}" )

# Exercise 2: Square roots and conjugates

# random integers
a = np.random.randint(-4, 5)
b = np.random.randint(a, a+5)
c = -sym.sqrt(b-a)


# create the expression
expr = sym.expand( sym.sqrt(x+b) + c ) / \
       sym.expand( (x+a) )


print(f'Compute the limit as x->{-a} of:\n')
expr

# plot the function
sym.plot(expr, (x, -10, 10))

# limits
print(f"Limit as x->{-a} from the left : {sym.limit(expr, x, -a, dir='-')}" )
print(f"Limit as x->{-a} from the right: {sym.limit(expr, x, -a, dir='+')}" )
print(f"Two-sided limit as x->{-a}     : {sym.limit(expr, x, -a, dir='+-')}" )
print(f"Function value at x={-a}       : {expr.subs(x, -a)}" )

# Exercise 3: Involving absolute values

# random integers
a, b = np.random.randint(-4, 5, 2)

# expression
expr = sym.Abs(x-a) + b
expr = (x-a) / sym.Abs(x-a)

print(f'Compute the limit as x->{a} of:\n')
expr

# plot the function
sym.plot(expr, (x, -10, 10))

# limits
print(f"Limit as x->{a} from the left : {sym.limit(expr, x, a, dir='-')}" )
print(f"Limit as x->{a} from the right: {sym.limit(expr, x, a, dir='+')}" )
print(f"Two-sided limit as x->{a}     : {sym.limit(expr, x, a, dir='+-')}" )
print(f"Function value at x={a}       : {expr.subs(x, a)}" )

