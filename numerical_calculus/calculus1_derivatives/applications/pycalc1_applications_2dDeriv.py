"""CodeChallenge: 2nd derivative test

COURSE: Master calculus 1 using Python: derivatives and applications
SECTION: Applications
LECTURE: CodeChallenge: 2nd derivative test
"""
import numpy as np
import sympy as sym
import matplotlib.pyplot as plt

from IPython.display import display, Math

# better image resolution
import matplotlib_inline.backend_inline as disPlay
disPlay.set_matplotlib_formats('svg')

# Exercise 1: Compute and plot the derivatives 

x = sym.symbols('x')

# the function and its derivatives
f = x**4 - 8*x**2
df = sym.diff(f, x)
ddf = sym.diff(f, x, 2)

# find f'=0
critPoints = np.array( sym.solve(df) )
critPoints

# lambdify and plot
f_l = sym.lambdify(x, f)
df_l = sym.lambdify(x, df)
ddf_l = sym.lambdify(x, ddf)

xx = np.linspace(-3, 3, 101)

plt.plot(xx, f_l(xx), label="f")
plt.plot(xx, df_l(xx), label="f'")
plt.plot(xx, ddf_l(xx), label="f''")
plt.plot(critPoints, df_l(critPoints), 'o', label="f'=0")
plt.plot(critPoints, ddf_l(critPoints), 'd', label="f''(f'=0)")
plt.plot(xx[[0, -1]], [0, 0], 'k--', linewidth=.2)

plt.ylim([-50, 50])
plt.xlim(xx[[0, -1]])
plt.legend()
plt.show()

# Exercise 2: Implement the 2nd derivative test

for cp in critPoints:

  # find the sign of the second derivative
  cpSign = np.sign( ddf_l(cp) )

  # print out the result
  if cpSign==-1:
    display(Math('d^2f(%s) < 0, \\text{ so it is a local maximum.}' %cp))
  elif cpSign==1:
    display(Math('d^2f(%s) > 0, \\text{ so it is a local minimum.}' %cp))
  elif cpSign==0:
    display(Math('d^2f(%s) = 0, \\text{ so the test is inconclusive.}' %cp))

# Exercise 3: Put it in a function

def secondDerivTest(f):

  # compute derivatives
  df = sym.diff(f, x)
  ddf = sym.diff(f, x, 2)

  # find f'=0
  critPoints = np.array( sym.solve(df) )

  # abort if no critical points!
  if len(critPoints)==0:
    print('No critical points! Aborting function!')
    return


  # lambdify and plot
  f_l = sym.lambdify(x, f)
  df_l = sym.lambdify(x, df)
  ddf_l = sym.lambdify(x, ddf)

  xx = np.linspace(-3, 3, 101)

  plt.plot(xx, f_l(xx), label=f"$f = {sym.latex(f)}$")
  plt.plot(xx, df_l(xx), label=f"$f' = {sym.latex(df)}$")
  plt.plot(xx, ddf_l(xx), label=f"$f'' = {sym.latex(ddf)}$")
  plt.plot(critPoints, df_l(critPoints), 'o', label="f'=0")
  plt.plot(critPoints, ddf_l(critPoints), 'd', label="f''(f'=0)")
  plt.plot(xx[[0, -1]], [0, 0], 'k--', linewidth=.2)

  plt.xlim(xx[[0, -1]])
  plt.legend()
  plt.show()

  # report the results of the 2nd derivative test
  for cp in critPoints:

    # find the sign of the second derivative
    cpSign = np.sign( ddf_l(cp) )

    # print out the result
    if cpSign==-1:
      display(Math('d^2f(%s) < 0, \\text{ so it is a local maximum.}' %cp))
    elif cpSign==1:
      display(Math('d^2f(%s) > 0, \\text{ so it is a local minimum.}' %cp))
    elif cpSign==0:
      display(Math('d^2f(%s) = 0, \\text{ so the test is inconclusive.}' %cp))

# test
f = x**4 - 8*x**2
secondDerivTest(f)

# Exercise 4: Try with a few different functions

secondDerivTest(x**4)

secondDerivTest(-x**4)

secondDerivTest(x**3)

secondDerivTest( 2*sym.pi*x + sym.sin(sym.pi*x) )
# problem is due to complex numbers; redefine x to have real=True

