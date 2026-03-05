"""CodeChallenge: Infinite derivatives exercises

COURSE: Master calculus 1 using Python: derivatives and applications
SECTION: Differentiation fundamentals
LECTURE: CodeChallenge: Infinite derivatives exercises
"""
import numpy as np
import sympy as sym
import matplotlib.pyplot as plt

# Exercise 1: Generate a random function

# create variable x
x = sym.symbols('x')

# random polynomial order
polyOrder = np.random.randint(1, 5)

# list of other functions to include
funList = [ sym.cos(x), sym.sin(x), sym.log(x), sym.exp(x) ]

# initialize the function
fx = 0

# add the polynomial terms
for i in range(polyOrder):
  fx += np.random.randint(-5, 6)*x**i

# add the transcendental functions
for f in np.random.choice(funList, 2, replace=False):
  fx += np.random.choice((-1, 1))*f

print(f'Differentiate this!\n')
fx

# Exercise 2: Lambdify and plot

# "default" domain
D = [-3, 3]

# possibly change start of domain
domain = sym.calculus.util.continuous_domain(fx, x, sym.S.Reals)
if domain.start==0:
  D[0] = .001

# convert expression to function
fxfun = sym.lambdify(x, fx)

# compute function values and empirical derivative
xx = np.linspace(D[0], D[1], 1234)
y  = fxfun(xx)
dy = np.diff(y) / np.mean(np.diff(xx))


# plot the function
_, axs = plt.subplots(2, 1, figsize=(6, 6))
axs[0].plot(xx, y, linewidth=2)
axs[0].set_title(f'$f(x)={sym.latex(fx)}$')

# and the derivative
axs[1].plot(xx[:-1], dy, linewidth=2)
axs[1].set_title('df')


# prettify both axes
for a in axs:
  a.set_xlim(xx[[0, -1]])
  a.set_xlabel('x')
  a.set_ylabel('y')


plt.tight_layout()
plt.show()

# Exercise 3: Derivative in sympy

print(f"Here's the derivative!\n")
sym.diff(fx)

