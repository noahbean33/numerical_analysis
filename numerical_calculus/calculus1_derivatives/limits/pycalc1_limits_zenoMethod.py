"""CodeChallenge: Limits via Zeno's paradox

COURSE: Master calculus 1 using Python: derivatives and applications
SECTION: Limits
LECTURE: CodeChallenge: Limits via Zeno's paradox
"""
import numpy as np
import sympy as sym
import matplotlib.pyplot as plt

# Exercise 1: implement the function

# a function for the function
def fx(u):
  return np.cos(u**2)**2 + np.pi

xx = np.linspace(-2.1, 2.1, 201)

plt.plot(xx, fx(xx))
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid()
plt.show()

# Exercise 2: Approximate the limit via Zeno's paradox

# target value (limit)
a = 1

# starting x-axis values
x0 = np.array([a-1, a+1])


# initialize
iterations = 10
limitvals = np.zeros((iterations, 2))
xAxisvals = np.zeros((iterations, 2))


# run the zeno's limit method in a for-loop
for i in range(iterations):

  # compute and store x0, y=f(x0)
  limitvals[i, :] = fx(x0)
  xAxisvals[i, :] = x0

  # update x-values (could this line be above the previous?)
  x0 = (x0+a)/2

# print out in a table
print('Limit from the left:')
print(np.vstack((xAxisvals[:, 0], limitvals[:, 0])).T)

print(' ')
print('Limit from the right:')
print(np.vstack((xAxisvals[:, 1], limitvals[:, 1])).T)

print(' ')
print(f'Function value at x={a}')
print(fx(a))

# Exercise 3: visualize the results

# and plot
plt.plot(xx, fx(xx), 'k')
plt.plot([a, a], [np.pi, 1+np.pi], 'k--', linewidth=.2)
plt.plot(xAxisvals, limitvals, 'o', markerfacecolor='w')
# plt.xlim([a-1, a+1]) # optional zoom in
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title(f'f({a}) = {fx(a)}')
plt.show()

