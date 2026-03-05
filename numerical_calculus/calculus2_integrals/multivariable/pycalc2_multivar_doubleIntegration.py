"""Multivariable indefinite integrals

COURSE: Master calculus 2 using Python: integration, intuition, code
SECTION: Multivariable integration
LECTURE: Multivariable indefinite integrals
"""
import numpy as np
import sympy as sym
import matplotlib.pyplot as plt

# symbolic variables
x, y, Cx, Cy = sym.symbols('x, y, Cx, Cy')

# the functions
Fxy = x + y**2
domain = [-10, 10]

Fxy = sym.sin(x)+sym.cos(y)
domain = [0, 2*np.pi]

# the two partial integrals
partInt_x = sym.integrate(Fxy, x)
partInt_y = sym.integrate(Fxy, y)

# let's see what they look like...
print('')
print('')

# now for the double integrals
partInt_yx = sym.integrate(partInt_y+Cy, x)
partInt_xy = sym.integrate(partInt_x+Cx, y)

# print them out
print('')

# # Visualizing a 2D function as a surface

# lambdify function
Fxy_l = sym.lambdify((x, y), Fxy)

# function domains for visualizations
xx = np.linspace(domain[0], domain[1], 41)
yy = np.linspace(domain[0], domain[1], 41)

# need a grid of points, not two vectors
XX, YY = np.meshgrid(xx, yy)
Z = Fxy_l(XX, YY)

# and draw
_, ax = plt.subplots(1, figsize=(8, 6))
ax.imshow(Z, extent=[xx[0], xx[-1], yy[-1], yy[0]], aspect='auto')
ax.set(xlabel='X', ylabel='Y')
ax.set_title(r'$f(x, y) = %s$' %sym.latex(Fxy))
plt.show()

# using plotly
import plotly.graph_objects as go

# create the surface plot
fig = go.Figure(data=[go.Surface(z=Z, x=XX, y=YY, colorscale='turbo')])

# modify the layout
fig.update_layout(width=800, height=600,
                  scene=dict(xaxis_title='X', yaxis_title='Y', zaxis_title='z = f(x, y)'))

fig.show()

# lambdify functions
Fxy_l = sym.lambdify((x, y), Fxy)
partInt_x_l = sym.lambdify((x, y), partInt_x)
partInt_y_l = sym.lambdify((x, y), partInt_y)
partInt_xy_l = sym.lambdify((x, y), partInt_xy) # C

# colorlimits
cbound = [-5, 5]

# visualize
_, axs = plt.subplots(2, 2, figsize=(12, 8))

axs[0, 0].imshow(Fxy_l(XX, YY), vmin=cbound[0], vmax=cbound[1], extent=[xx[0], xx[-1], yy[-1], yy[0]], aspect='auto', cmap='turbo')
axs[0, 0].set_title(r'$f(x, y) = %s$' %sym.latex(Fxy))

axs[0, 1].imshow(partInt_xy_l(XX, YY), vmin=cbound[0], vmax=cbound[1], extent=[xx[0], xx[-1], yy[-1], yy[0]], aspect='auto', cmap='turbo')
axs[0, 1].set_title(r'$F_{xy} = %s$' %sym.latex(partInt_xy))

axs[1, 0].imshow(partInt_x_l(XX, YY), vmin=cbound[0], vmax=cbound[1], extent=[xx[0], xx[-1], yy[-1], yy[0]], aspect='auto', cmap='turbo')
axs[1, 0].set_title(r'$F_x = %s$' %sym.latex(partInt_x))

axs[1, 1].imshow(partInt_y_l(XX, YY), vmin=cbound[0], vmax=cbound[1], extent=[xx[0], xx[-1], yy[-1], yy[0]], aspect='auto', cmap='turbo')
axs[1, 1].set_title(r'$F_y = %s$' %sym.latex(partInt_y))

# axis labels
for a in axs.flatten(): a.set(xlabel='x', ylabel='y')

plt.tight_layout()
plt.show()

