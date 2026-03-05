"""CodeChallenge: Gradient descent in 2D

COURSE: Master calculus 1 using Python: derivatives and applications
SECTION: Multivariable differentiation
LECTURE: CodeChallenge: Gradient descent in 2D
"""
import numpy as np
import sympy as sym
import matplotlib.pyplot as plt

import matplotlib_inline.backend_inline
matplotlib_inline.backend_inline.set_matplotlib_formats('svg')

# Exercise 1: Implement the function in numpy

# the "peaks" function
def peaks(xi, yi):
  # expand to a 2D mesh
  X, Y = np.meshgrid(xi, yi)
  
  z = 3*(1-X)**2 * np.exp(-(X**2) - (Y+1)**2) \
      - 10*(X/5 - X**3 - Y**5) * np.exp(-X**2-Y**2) \
      - 1/3*np.exp(-(X+1)**2 - Y**2)
  return z

# create the landscape
xi = np.linspace(-3, 3, 201)
yi = np.linspace(-3, 3, 201)

Z = peaks(xi, yi)

# let's have a look!
plt.imshow(Z, extent=[xi[0], xi[-1], yi[0], yi[-1]], vmin=-5, vmax=5, origin='lower')
plt.show()

# Exercise 2: Compute the derivative in sympy

# create derivative functions using sympy

x, y = sym.symbols('x, y')

# rewrite in sympy (using Zs preserve variable Z)
Zs = 3*(1-x)**2 * sym.exp(-(x**2) - (y+1)**2) \
    - 10*(x/5 - x**3 - y**5) * sym.exp(-x**2-y**2) \
    - 1/3*sym.exp(-(x+1)**2 - y**2)


# create functions from the sympy-computed derivatives
df_x = sym.lambdify( (x, y), sym.diff(Zs, x) )
df_y = sym.lambdify( (x, y), sym.diff(Zs, y) )

df_x(1, 1)

_, axs = plt.subplots(1, 3, figsize=(8, 6))

axs[0].imshow(Z, extent=[xi[0], xi[-1], yi[0], yi[-1]], vmin=-5, vmax=5, origin='lower')
axs[0].set_title('$f(x, y)$')

# Note: There was a bug in the code I wrote in the video; the expansion to vector should be on yi, not xi.
axs[1].imshow(df_x(xi, yi[:, None]), extent=[xi[0], xi[-1], yi[0], yi[-1]], vmin=-5, vmax=5, origin='lower')
axs[1].set_title('$f_x$')

axs[2].imshow(df_y(xi, yi[:, None]), extent=[xi[0], xi[-1], yi[0], yi[-1]], vmin=-5, vmax=5, origin='lower')
axs[2].set_title('$f_y$')

plt.tight_layout()
plt.show()

# Exercise 3: Gradient descent

# random starting point (uniform between -2 and +2)
localmin = np.random.rand(2)*4-2 # also try specifying coordinates
startpnt = localmin[:] # make a copy, not re-assign

# learning parameters
learning_rate = .01
training_epochs = 1000

# run through training
trajectory = np.zeros((training_epochs, 2))
for i in range(training_epochs):
  grad = np.array([ df_x(localmin[0], localmin[1]), 
                    df_y(localmin[0], localmin[1])
                  ])
  localmin = localmin - learning_rate*grad
  trajectory[i, :] = localmin


print(localmin)
print(startpnt)

# let's have a look!
plt.imshow(Z, extent=[xi[0], xi[-1], yi[0], yi[-1]], vmin=-5, vmax=5, origin='lower')
plt.plot(startpnt[0], startpnt[1], 'bs')
plt.plot(localmin[0], localmin[1], 'ro')
plt.plot(trajectory[:, 0], trajectory[:, 1], 'r')
plt.legend(['rnd start', 'local min'])
plt.colorbar()
plt.show()

# Exercise 4: Gradient ascent

# solution is to add the learning_rate*grad instead of subtract

# Exercise 5: Find exact solutions

# derivatives
sdx = sym.diff(Zs, x)
sdy = sym.diff(Zs, y)

sym.solve(sdx, x)

