"""Calculart! Fun and beauty with calculus :)

COURSE: Master calculus 2 using Python: integration and applications
SECTION: Intuition for integration
LECTURE: Calculart! Fun and beauty with calculus :)
"""
import numpy as np
import sympy as sym
import matplotlib.pyplot as plt

# # Calculart 1: Sinc function

# define the function
x = sym.symbols('x')

# symbolic expressions for the function, its integral, and its derivative
fx   = sym.sin(x) / x
intf = sym.integrate(fx)
df   = sym.diff(fx)

# have a quick look...
sym.plot(fx, intf, df, title=fx, legend=True)

# lambdify
fx_l = sym.lambdify(x, fx)
intf_l = sym.lambdify(x, intf)
df_l = sym.lambdify(x, df)

# plot in matplotlib
xx = np.linspace(-10, 10, 200)
plt.plot(intf_l(xx), fx_l(xx), linewidth=2, color=[.2, 0, .4])
plt.plot(intf_l(xx), -fx_l(xx)-.5, linewidth=2, color=[.4, 0, .2])
plt.plot(.94*intf_l(xx)+.02, -fx_l(xx)-.5-.02, linewidth=1, color=[.7, .7, .7], zorder=-3)

# export as png with transparency
plt.axis('off')
plt.savefig('sincMoustache.png', transparent=True, dpi=300)
plt.show()

fig = plt.figure()
fig.patch.set_facecolor('black')

plt.scatter(fx_l(xx), intf_l(xx), c=df_l(xx), cmap='PuRd')
plt.scatter(-fx_l(xx)-.5, intf_l(xx), c=-df_l(xx), cmap='PuBuGn')

plt.axis('off')
plt.show()

# # Calculart 2: log by secant

fx = sym.log(x) * sym.cos(x)**2
intf = sym.integrate(fx)
df = sym.diff(fx)
sym.plot(fx, intf, df, ylim=[-5, 5], title=fx, legend=True)

# lambdify and plot in matplotlib
fx_l = sym.lambdify(x, fx)
intf_l = sym.lambdify(x, intf)
df_l = sym.lambdify(x, df)

xx = np.linspace(.8, 20, 200)
plt.scatter(fx_l(xx), intf_l(xx), c=df_l(xx), cmap='PuRd')
plt.scatter(-fx_l(xx)-.15, intf_l(xx), c=df_l(xx), cmap='PuBuGn')

plt.axis('off')
plt.show()

# # Calculart 3: Warholified rectangles

# define some dx's
dxs = [ 1, .5, 1.5, .2, .4, .8 ]

# the function to use
fx = sym.lambdify( x, sym.cos(x)/x )

### make the art!
warholColors = [ '#03BFAC', '#75DFCA', '#1DBACC', '#ED3192', '#087FBF' ]
# Color codes from https://color.adobe.com/POP-ART-COLORS-6-color-theme-7944850/

# setup the figure
fig, axs = plt.subplots(2, 3, figsize=(12, 6))
fig.subplots_adjust(hspace=0, wspace=0)
axs = axs.flatten()

for idx, dx in enumerate(dxs):

  # define the resolution and plot the rectangles
  xx = np.arange(-10, 10+dx, dx)
  for xi in xx:
    axs[idx].fill_between([xi-dx/2, xi+dx/2], [fx(xi), fx(xi)], edgecolor='k', linewidth=.3,
                          facecolor=warholColors[idx%len(warholColors)])

  # adjust the axes
  axs[idx].set_facecolor(warholColors[(idx-1)%len(warholColors)])
  axs[idx].set(ylim=[-.8, 1], xticks=[], yticks=[])
  axs[idx].spines[['left', 'bottom']].set_visible(False)

plt.show()

