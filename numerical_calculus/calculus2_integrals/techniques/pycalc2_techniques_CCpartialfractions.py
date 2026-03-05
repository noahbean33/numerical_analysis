"""CodeChallenge: Partial fractions algorithm

COURSE: Master calculus 2 using Python: integration, intuition, code
SECTION: Integration techniques
LECTURE: CodeChallenge: Partial fractions algorithm
"""
import numpy as np
import sympy as sym
import matplotlib.pyplot as plt

x, A, B = sym.symbols('x, A, B')

# function
fx = (5*x+3) / (2*x**2 - 4*x - 6)

# quickie-plot
sym.plot(fx, (x, -5, 5), ylim=[-20, 20])
plt.show()

print('')

# Step 1: separate numerator and denominator
numerator, denominator = fx.as_numer_denom()

# and print

# Step 2: factor the denominator
den_factors = sym.factor(denominator)

# print them out
for i, fact in enumerate(den_factors.args):
  print('')

# Step 3: create simple fractions
simple_fract_1 = A / (den_factors.args[0]*den_factors.args[1])
simple_fract_2 = B / den_factors.args[2]

print('')

# Step 4: solve for A and B
expression = sym.Eq(numerator , simple_fract_1*sym.prod(den_factors.args) + simple_fract_2*sym.prod(den_factors.args) )
solutionsAB = sym.solve(expression, (A, B))

solutionsAB

# Step 5: integrate separately
defint1 = sym.integrate( simple_fract_1.subs(A, solutionsAB[A]) )
defint2 = sym.integrate( simple_fract_2.subs(B, solutionsAB[B]) )

print('')

# Step 6: sum the parts
mysolution = defint1 + defint2
mysolution

# Step 7: compare against sympy integration from the original function
symsolution = sym.integrate(fx)
symsolution

