"""CodeChallenge: partial and double integrals

COURSE: Master calculus 2 using Python: integration, intuition, code
SECTION: Multivariable integration
LECTURE: CodeChallenge: partial and double integrals
"""
import numpy as np
import sympy as sym
import matplotlib.pyplot as plt

# Exercise 1: A function and its partial integrals

# symbolic variables
x, y, Cx, Cy = sym.symbols('x, y, Cx, Cy')

# the function
Fxy = sym.cos(x) * (x**2 * y) # for Exercises 1-4
# Fxy = sym.exp( -(x**2+y**2) ) # 2D Gaussian for Exercise 5

# the two partial integrals
partInt_x = sym.integrate(Fxy, x)
partInt_y = sym.integrate(Fxy, y)

# let's see what they look like...
print('')
print('')

# For Exercise 5: ask ChatGPT about the erf() function!

# Exercise 2: Double integrals

# now for the double integrals
partInt_yx = sym.integrate(partInt_y+Cy, x)
partInt_xy = sym.integrate(partInt_x+Cx, y)

# print them out
print('')

# Exercise 3: Visualizations

# lambdify functions
Fxy_l = sym.lambdify((x, y), Fxy)
partInt_x_l = sym.lambdify((x, y), partInt_x)
partInt_y_l = sym.lambdify((x, y), partInt_y)
partInt_xy_l = sym.lambdify((x, y), sym.integrate(partInt_x, y)) # redo integration without the constant

# function domains for visualizations
xx = np.linspace(-np.pi, 2*np.pi, 41)
yy = np.linspace(-1, 2, 41)

# need a grid of points, not two vectors
XX, YY = np.meshgrid(xx, yy)

# Note the difference between xx and XX
print('Vector xx:')
print(np.round(xx, 3))

print('')
print('Matrix XX:')
print(np.round(XX, 3))

# colorlimits
cbound = [-5, 5] # for Exercises 1-4
cbound = [-.5, .5] # for the Gaussian in Exercise 5

# visualize
_, axs = plt.subplots(2, 2, figsize=(12, 8))

axs[0, 0].imshow(Fxy_l(XX, YY), vmin=cbound[0], vmax=cbound[1], extent=[xx[0], xx[-1], yy[-1], yy[0]], aspect='auto')
axs[0, 0].set_title(r'$f(x, y) = %s$' %sym.latex(Fxy))

axs[0, 1].imshow(partInt_xy_l(XX, YY), vmin=cbound[0], vmax=cbound[1], extent=[xx[0], xx[-1], yy[-1], yy[0]], aspect='auto')
axs[0, 1].set_title(r'$F_{xy} = %s$' %sym.latex(partInt_xy))

axs[1, 0].imshow(partInt_x_l(XX, YY), vmin=cbound[0], vmax=cbound[1], extent=[xx[0], xx[-1], yy[-1], yy[0]], aspect='auto')
axs[1, 0].set_title(r'$F_x = %s$' %sym.latex(partInt_x))

axs[1, 1].imshow(partInt_y_l(XX, YY), vmin=cbound[0], vmax=cbound[1], extent=[xx[0], xx[-1], yy[-1], yy[0]], aspect='auto')
axs[1, 1].set_title(r'$F_y = %s$' %sym.latex(partInt_y))

# axis labels
for a in axs.flatten(): a.set(xlabel='x', ylabel='y')

plt.tight_layout()
plt.show()

# Exercise 4: Floating surfaces

# using 3d axis from matplotlib
from mpl_toolkits.mplot3d import Axes3D

# surface landscape
Z = Fxy_l(XX, YY)

# create a figure object and add a 3D subplot
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

# draw the surface
surf = ax.plot_surface(XX, YY, Z, cmap='turbo', alpha=.9, vmin=cbound[0], vmax=cbound[1])

# add a colorbar
fig.colorbar(surf, shrink=.5, label='z = f(x, y)')

ax.set(xlabel='X', ylabel='Y', zlabel='f(x, y)')
plt.show()

# again using plotly
import plotly.graph_objects as go

# create the surface plot
fig = go.Figure(data=[go.Surface(z=Z, x=XX, y=YY, colorscale='turbo', cmin=cbound[0], cmax=cbound[1])])

# modify the layout
fig.update_layout(title='Surface representation of function', width=800, height=600,
                  scene=dict(
                      xaxis_title='X',
                      yaxis_title='Y',
                      zaxis_title='Z = f(x, y)'
                  ))

fig.show()

