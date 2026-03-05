"""CodeChallenge: infinite practice problems

COURSE: Master calculus 2 using Python: integration, intuition, code
SECTION: Integrating functions
LECTURE: CodeChallenge: infinite practice problems
"""
import numpy as np
import sympy as sym
import matplotlib.pyplot as plt

# Exercise 1: Antiderivatives of polynomials

# create symbolic variable
x, C = sym.symbols('x, C')

# initialize terms
nTerms = np.random.randint(2, 5)
coefs = np.random.randint(-10, 11, nTerms)

# initialize the expression
expr = 0

# build the equation one term at a time
for i, c in enumerate(coefs):

  # randomly scale odd exponents by 2
  if i%2==1:
    scalar = np.random.choice([1, 2], 1)[0]

  # randomly scale even exponentials by -1
  else:
    scalar = np.random.choice([-1, 1], 1)[0]

  # add this term to the expression
  expr += c * x**sym.Rational(i, scalar)

# let's have a quick look :)
expr

# display the problem
print('')

# use sympy to get the answer
ans = sym.integrate(expr, x) + C

# display the answer
print('')

np.random.randint(-3, 4, 2)

# Exercise 2: Definite integrals of polynomials

# create symbolic variable
x, C = sym.symbols('x, C')

# initialize terms
nTerms = np.random.randint(2, 5)
coefs = np.random.randint(-10, 11, nTerms)

# create bounds (must be sorted and unequal)
a, b = np.sort(np.random.randint(-3, 4, 2))
if a==b: b+=1 # just add 1

# initialize the expression
expr = 0

# build the equation one term at a time
for i, c in enumerate(coefs):

  # randomly scale odd exponents by 2
  if i%2==1:
    scalar = np.random.choice([1, 2], 1)[0]

  # randomly scale even exponentials by -1
  else:
    scalar = np.random.choice([-1, 1], 1)[0]

  # add this term to the expression
  expr += c * x**sym.Rational(i, scalar)

# because we're dealing only with real numbers, we don't want negative radicals
radical = 0
for term in expr.as_ordered_terms():
  try:
    radical += not term.args[-1].args[-1].is_integer
  except:
    pass

# if there are negative radicals, force bounds to be positive
if radical>0:
  a, b = np.sort(np.abs([a, b]))

# and let's have a quick look
expr

# an elucidation of the code to extract powers
print(expr)
print('')

for term in expr.as_ordered_terms():
  print(f'Current term is {term}')
  try:
    print(f'  The exponent is {term.args[-1].args[-1]}')
    print(f'  Is a radical? {not term.args[-1].args[-1].is_integer}')
  except:
    None
  print('')

# display the problem
print('')

# use sympy to get the answer
ans = sym.integrate(expr, (x, a, b))

# display the answer
print('')

# Exercise 3: Initial value problems

# create a random differential equation
df = np.random.randint(-5, 6)*x + np.random.randint(-5, 6)

# create the initial conditions
initial_vals = np.random.randint(-5, 6, 2) # first number is x_0, second number is f(x_0)

# print the problem

# and the solution!

# step 1: integrate to find f(x)
fx = sym.integrate(df, x) + C

# step 2: solve for C
constant = sym.solve( fx.subs(x, initial_vals[0]) - initial_vals[1] , C)[0]

# print the results!

