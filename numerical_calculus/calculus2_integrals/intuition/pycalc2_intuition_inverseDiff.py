"""Integration as "inverse differentiation"

COURSE: Master calculus 2 using Python: integration and applications
SECTION: Intuition for integration
LECTURE: Integration as "inverse differentiation"
"""
import numpy as np
import matplotlib.pyplot as plt

# # Discrete differences (approx of derivative)

# x-axis grid on which to evaluate the function
x = np.linspace(-1, 4, 301)

# define a function
fx = x**2

# find the x-axis coordinate of x=0
zeroIdx = np.argmin(abs(x-0))

# visualize the function
plt.plot(x, fx, 'ks', markerfacecolor='w', alpha=.4, markersize=10, linewidth=2)
plt.xlabel('x')
plt.ylabel('y = f(x)')
plt.show()

# difference (discrete derivative)
dx = x[1] - x[0]
df = np.diff(fx) / dx

# visualize the derivative
plt.plot(x[:-1], df, 'ks', markerfacecolor='w', alpha=.4, markersize=10, linewidth=2)
plt.xlabel('x')
plt.ylabel('dy/dx')
plt.show()

# # About the cumulative sum

# a brief aside on the cumulative sum

v = np.arange(10)
print('The vector:')
print(v)

# take the sum
regularSum = np.sum(v)
print('')
print('"Regular" sum:')
print(regularSum)

# cumulative sum via for-loop
cumulativeSum = np.zeros(len(v), dtype=int)
for i in range(len(v)):
  cumulativeSum[i] = np.sum( v[:i+1] )

print('')
print('Cumulative sum via for-loop:')
print(cumulativeSum)

# cumulative sum via function
cumulativeSumF = np.cumsum( v )
print('')
print('Cumulative sum via formula:')
print(cumulativeSumF)

# # Approximation of the integral using cumulative sum

# cumulative sum (discrete integral)
idf = np.cumsum(df) * dx
idf -= idf[zeroIdx] # normalize so that idf(0)=0
idf += fx[zeroIdx]  # then add constant from original function

# visualize the integral
plt.plot(x[:-1], idf, 'ks', markerfacecolor='w', alpha=.4, markersize=10, linewidth=2, label='Integral of df')

# and plot the original function on top
plt.plot(x, fx, 'm', linewidth=3, label='f(x)')

plt.legend()
plt.xlabel('x')
plt.ylabel(r"y = $\int f' dx$")
plt.show()

