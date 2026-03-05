"""CodeChallenge: Drawing discrete integrals

COURSE: Master calculus 2 using Python: integration and applications
SECTION: Intuition for integration
LECTURE: CodeChallenge: Drawing discrete integrals
"""
import numpy as np
import matplotlib.pyplot as plt

# Exercise 1: Functions to compute and plot the integral

# create a function that computes and outputs the derivative and integral
def derivAndIntegral(x, fx):

  # difference (discrete derivative)
  dx = x[1] - x[0]
  df = np.diff(fx) / dx

  # cumulative sum (discrete integral)
  idf = np.cumsum(df) * dx

  # normalize the integral
  zeroIdx = np.argmin(abs(x-0)) # x-axis coordinate of x=0
  idf -= idf[zeroIdx] # set idf(0)=0
  idf += fx[zeroIdx]  # then add constant from original function

  # return the calculations
  return df, idf

# and a function that does the plotting
def plotTheFunctions():
  _, axs = plt.subplots(1, 3, figsize=(12, 4))

  # visualize the function
  axs[0].plot(x, fx, 'ks', markerfacecolor='w', markersize=10, linewidth=2, alpha=.5)
  axs[0].set(xlabel='x', ylabel='y = f(x)', title='Original function')

  # visualize the derivative
  axs[1].plot(x[1:], df, 'ks', markerfacecolor='w', markersize=10, linewidth=2, alpha=.5)
  axs[1].set(xlabel='x', ylabel='dy/dx', title='Discrete derivative')

  # visualize the integral
  axs[2].plot(x[1:], idf, 'ks', markerfacecolor='w', markersize=10, linewidth=2, label='Integral approx.', alpha=.5)

  # and plot the original function on top
  axs[2].plot(x, fx, 'm', linewidth=3, label='Orig. func.')
  axs[2].set(xlabel='x', ylabel=r'y = $\int df/dx$', title='Cumulative sum of derivative')
  axs[2].legend()

  plt.tight_layout()
  plt.show()

# # Confirm with x**2

# x-axis grid and function
x = np.linspace(-1, 4, 301)
fx = x**2

df, idf = derivAndIntegral(x, fx)
plotTheFunctions()

# Exercise 2: Explore some other functions

# x-axis grid and function
x = np.linspace(-1, 4, 73)
fx = x**3 + 4

# another option
x = np.linspace(-np.pi, np.pi, 193)
fx = x**3/10 - np.pi*np.exp(-x**2) + np.sin(4*x)

df, idf = derivAndIntegral(x, fx)
plotTheFunctions()

