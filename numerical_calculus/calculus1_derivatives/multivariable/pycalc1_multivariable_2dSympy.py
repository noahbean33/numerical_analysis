"""CodeChallenge: 2D functions in sympy

COURSE: Master calculus 1 using Python: derivatives and applications
SECTION: Multivariable differentiation
LECTURE: CodeChallenge: 2D functions in sympy
"""
import numpy as np
import sympy as sym
import matplotlib.pyplot as plt

# use plotly for 3D plotting
import plotly.graph_objects as go

# Exercise 1: Create and evaluate a 2D function

x, y = sym.symbols('x, y')

# create the function
fxy = x**2 + sym.sin(y)
fxy

# solve for specific values of x
fxy.subs(x, 4)

# solve for specific values of y
fxy.subs(y, sym.pi/2)

# solve for specific values of x and y
fxy.subs({x:4, y:sym.pi/2})

# Exercise 2: Visualize that 2D function

sym.plotting.plot3d(fxy, (x, -1.5, 1.5), (y, -sym.pi, sym.pi),
                    title=f'$f(x, y) = {sym.latex(fxy)}$')
plt.show()

# Exercise 3: That cool wavey surface

fxy = sym.sin(x + y**2)

# draw it in sympy
sym.plotting.plot3d(fxy, (x, -sym.pi, sym.pi), (y, -sym.pi, sym.pi));

# lambdify expression
fxy_lam = sym.lambdify((x, y), fxy)

# and evaluate at specific points
xx = np.linspace(-np.pi, np.pi, 40)
X, Y = np.meshgrid(xx, xx)
Z = fxy_lam(X, Y)

fig = go.Figure(data=[go.Surface(x=xx, y=xx, z=Z)])
fig.update_layout(autosize=False)
fig.show()

# Exercise 4: A quintovariable equation

x, y, f, phi, sigma = sym.symbols('x, y, f, phi, sigma')

# sine wave initializations
U = x*sym.cos(phi) + y*sym.sin(phi)

# create the sine wave and Gaussian
sine2d = sym.sin( 2*sym.pi*f*U )
gaus2d = sym.exp(-(x**2 + y**2) / (2*sigma**2))

# point-wise multiply the sine and Gaussian
fxy = sine2d * gaus2d


# print out the function
fxy

# create one instance of the function for specific variables
Z = fxy.subs({
                  f : .05,      # sine frequency
                phi : sym.pi/4, # rotation
              sigma : 3*sym.pi  # width of Gaussian
              })


# draw it in sympy
sym.plotting.plot3d(Z, (x, -30, 30), (y, -30, 30),
                    title=f'$f(x, y) = {sym.latex(Z)}$');

