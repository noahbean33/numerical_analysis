"""CodeChallenge: Convergence and divergence

COURSE: Master calculus 2 using Python: integration, intuition, code
SECTION: Improper integrals
LECTURE: CodeChallenge: Convergence and divergence
"""
import numpy as np
import sympy as sym
import matplotlib.pyplot as plt
import scipy.integrate as spi

# Exercise 1: Integrals from previous video

x = sym.symbols('x')

#          function     lower limit    upper limit
funs = [ [ 1/x**2      ,    1       ,    sym.oo  ],
         [ sym.pi/x**3 ,    1       ,    sym.oo  ],
         [ x**4        ,   -sym.oo  ,    -1      ],
         [ 1/sym.sqrt(x),   1       ,    sym.oo  ]
]

# calculate and print their integral
for fi in range(len(funs)):

  # extract the information
  f = funs[fi][0]
  limL = funs[fi][1]
  limU = funs[fi][2]

  # compute the integral
  int2display = sym.Integral(f, (x, limL, limU)) # for visualization
  defint = sym.integrate(f, (x, limL, limU))

  # and display
  print('')

# Exercise 2: A range of p's

# the range of p-values
pvalues = np.linspace(-3, 1, 21)

# range of x-axis grid locations for plotting
xx = np.linspace(.01, 10, 301)

# loop over exponents
_, axs = plt.subplots(1, 2, figsize=(14, 4))
for p in pvalues:

  # get the indefinite integral of the function
  F = sym.integrate(x**p)

  # use FTC-2 to determine whether it converges or diverges
  defint = F.subs(x, sym.oo) - F.subs(x, 1)

  # pick color based on integral
  c='g' if defint.is_finite else 'r'

  # lambdify and visualize
  F_l = sym.lambdify(x, F)
  axs[0].plot(xx, F_l(xx), c, linewidth=np.abs(p))

  # plot the convergence
  axs[1].plot(p, 1-defint.is_finite, 's', color=c, markersize=12)

axs[0].set(xlabel='x', xlim=xx[[0, -1]], ylabel='y = F(x)', ylim=[-15, 30], title='Indefinite integral functions')
axs[1].set(yticks=[0, 1], yticklabels=['Converges', 'Diverges'], xlabel=r'$p$ in $x^{p}$', ylim=[-.5, 1.5], title='Definite integral convergence')

plt.tight_layout()
plt.show()

