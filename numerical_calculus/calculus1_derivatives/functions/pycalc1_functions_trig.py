"""CodeChallenge: Trigonometry

COURSE: Master calculus 1 using Python: derivatives and applications
SECTION: Functions
LECTURE: CodeChallenge: Trigonometry
"""
import numpy as np
import sympy as sym
import matplotlib.pyplot as plt

# Exercise 1: fun with trig :)

xx = np.linspace(-np.pi, 2*np.pi, 234)

# functions
f = [0]*3

#     function def       label
f[0] = np.sin(xx)     , 'sin(x)'
f[1] = np.sin(xx)**2  , 'sin(x)**2'
f[2] = np.sin(xx**2)  , 'sin(x**2)'

# and plot
for fun, label in f:
  plt.plot(xx, fun, linewidth=2, label=label)
plt.xlabel('Angle (rad.)')
plt.ylabel('y=f(x)')
plt.legend(bbox_to_anchor=(1, 1))
plt.show()

# Exercise 2: More fun with trig :)

# functions
f = [0]*3

#       function def           label
f[0] = np.sin(np.cos(xx))  , 'sin(cos(x))'
f[1] = np.cos(np.sin(xx))  , 'cos(sin(x))'
f[2] = np.cos(xx)          , 'cos(x)'

# and plot
for fun, label in f:
  plt.plot(xx, fun, linewidth=2, label=label)
plt.xlabel('Angle (rad.)')
plt.ylabel('y=f(x)')
plt.legend(bbox_to_anchor=(1, 1))
plt.show()

# Exercise 3: resolution and tan

for i in range(2, 5):
  xx = np.linspace(0, 2*np.pi, 10**i)
  plt.plot(xx, np.tan(xx), '.-', label=f'{10**i} pnts')

# plt.ylim([-500, 500])
# plt.xlim([1.55, 1.6])
plt.legend()
plt.xlabel('Angle (rad.)')
plt.ylabel('y=f(x)')
plt.show()

