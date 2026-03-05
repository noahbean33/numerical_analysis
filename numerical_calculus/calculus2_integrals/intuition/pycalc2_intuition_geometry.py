"""Integration as geometric area

COURSE: Master calculus 2 using Python: integration and applications
SECTION: Intuition for integration
LECTURE: Integration as geometric area
"""
import numpy as np
import matplotlib.pyplot as plt

# # Create a function and evaluate it

# function for the function
def fx(u):
  return u**2 - .5

# define the grid spacing
dx = .2

# x-axis grid in spacing of dx
xx = np.arange(-1, 1+dx, dx)

# evaluate the function at those points
y = fx(xx)

# make a table of x, y pairs
print('   x    |    y')
print('--------|--------')
for xi, yi in zip(xx, y):
  print(f'{xi:>6.3f}  |  {yi:>6.3f}')

# # Visualize the function and its approximate area

# plot the function
plt.figure(figsize=(8, 5))
plt.plot(xx, y, 'ks-', linewidth=2, markersize=10, markerfacecolor=[.7, .3, .9])

# initialize area
area = 0

# plot rectangles
for xi in xx:

  # draw the rectangle
  plt.fill_between([xi-dx/2, xi+dx/2], [fx(xi), fx(xi)], edgecolor='k', facecolor=[.9, .8, .9])

  # sum the area
  area += fx(xi)*dx

# finish the figure
plt.title(f'Area of boxes = {area:.2f}')
plt.xlabel('x')
plt.ylabel('$f(x) = x^2$')
plt.show()

