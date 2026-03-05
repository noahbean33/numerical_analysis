"""CodeChallenge: farmers and Qberts

COURSE: Master calculus 1 using Python: derivatives and applications
SECTION: Applications
LECTURE: CodeChallenge: farmers and Qberts
"""
import numpy as np
import sympy as sym
import matplotlib.pyplot as plt

# Exercise 1: The farmer's fence

# create symbolic variables
x = sym.symbols('x')

# y in terms of x
y = 400/x

# define cost function
C = 2*x + 3*y/2
C

# quick plot of cost as function of x
sym.plot(C, (x, 3, 70), ylim=[50, 150])

# derivative of cost function
dC = sym.diff(C)

# solve x in dA=0
solX = sym.solve(dC, x)
print(solX)

# but we only need the positive solution
solX = solX[1]
solX

# then solve for y
solY = y.subs(x, solX)
solY

# lambda functions to plot the data in matplotlib
xx = np.linspace(3, 70, 2001)

C_lambda  = sym.lambdify(x, C)
dC_lambda = sym.lambdify(x, dC)

# plot the function
_, axs = plt.subplots(2, 1, figsize=(8, 5))
axs[0].plot(xx, C_lambda(xx), linewidth=2)
axs[0].plot(solX, C_lambda(solX), 'ro')
axs[0].set_xlim(xx[[0, -1]])
axs[0].set_ylim([50, 150])
axs[0].set_xlabel('Length of side x')
axs[0].set_ylabel('Cost')
axs[0].set_title('Cost as a function of side length')

# plot the derivative
axs[1].plot(xx, dC_lambda(xx), linewidth=2)
axs[1].plot(xx[[0, -1]], [0, 0], '--', color=[.6, .6, .6])
axs[1].plot(solX, dC_lambda(solX), 'ro')
axs[1].set_xlim(xx[[0, -1]])
axs[1].set_ylim([-10, 5])
axs[1].set_xlabel('Length of side x')
axs[1].set_ylabel('dC/dx')

plt.tight_layout()
plt.show()

# (out of curiosity) confirm area and calculate perimeter and cost
print(f'Confirm area = {solX*solY} m^2')
print(f'Total fence  = {sym.N(2*solX + 2*solY):.2f} meters')
print(f"Fred's cost  = {sym.N(2*solX + 3*solY/2)*100:.2f} euros")
print(f"Fran's cost  = {sym.N(solY/2)*100:.2f} euros")

# Exercise 2: Qbert's cost-saving

# need to redefine y as its own variable
y = sym.symbols('y')

# volume function
V = x**2 * y - 200

# solve for y
yInTermsOfX = sym.solve(V, y)[0]

# surface area
S = x**2 + 4*x*yInTermsOfX
S

# derivative of S and solve for x
dS = sym.diff(S)
solX = sym.solve(dS, x)
solX

# then solve for y
solY = yInTermsOfX.subs(x, solX[0])
solY

# surface areas of the two sides sizes
print(f'Surface area of the bottom: {sym.N(solX[0]**2):.3f} cm^2')
print(f'Surface area of one side: {sym.N(solX[0]*solY):.3f} cm^2')
print(f'Surface area of all sides: {4*sym.N(solX[0]*solY):.3f} cm^2')

# lambda functions to plot the data in matplotlib
xx = np.linspace(2, 40, 2001)

A_lambda  = sym.lambdify(x, S)
dA_lambda = sym.lambdify(x, sym.diff(S))

# plot the function
_, axs = plt.subplots(2, 1, figsize=(8, 5))
axs[0].plot(xx, A_lambda(xx), linewidth=2)
axs[0].plot(solX[0], A_lambda(solX[0]), 'ro')
axs[0].set_xlim(xx[[0, -1]])
axs[0].set_ylim([0, 1500])
axs[0].set_xlabel('Length of side x')
axs[0].set_ylabel('Area')
axs[0].set_title('Surface area as a function of side length')

# plot the derivative
axs[1].plot(xx, dA_lambda(xx), linewidth=2)
axs[1].plot(xx[[0, -1]], [0, 0], '--', color=[.6, .6, .6])
axs[1].plot(solX[0], dA_lambda(solX[0]), 'ro')
axs[1].set_xlim(xx[[0, -1]])
axs[1].set_ylim([-100, 100])
axs[1].set_xlabel('Length of side x')
axs[1].set_ylabel('dV/dx')

plt.tight_layout()
plt.show()

