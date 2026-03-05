"""CodeChallenge: product and quotient rules, and chain rule

COURSE: Master calculus 1 using Python: derivatives and applications
SECTION: Differentiation rules and theorems
LECTURE: CodeChallenge: product and quotient rules, and chain rule
"""
import numpy as np
import sympy as sym
import matplotlib.pyplot as plt

# better image resolution
import IPython
IPython.matplotlib_inline.backend_inline.set_matplotlib_formats('svg')

# Exercise 1: Confirm the product rule

# create symbolic variable
x = sym.symbols('x')

# create functions
f = x**2
g = sym.cos(x)

# and their derivatives
df = sym.diff(f)
dg = sym.diff(g)

# their combination
fg = f*g
dfg = sym.diff(fg)

# "manual" product rule
man_dfg = df*g + f*dg

# print them out
from IPython.display import display # for nicer in-line printing

print(f"(fg)':")
display(dfg)

print(f"\nf'g + fg':")
display(man_dfg)

# Exercise 2: Confirm the quotient rule

# using the functions defined earlier

# their combination
fg = f/g
dfg = sym.diff(fg)

# "manual" quotient rule
man_dfg = (df*g - f*dg) / g**2

print(f"(f/g)':\n")
display(dfg)

print(f"\n\n(f'g - fg')/(g**2)':\n")
display(man_dfg)

sym.simplify(man_dfg)

# Exercise 3: Derivative of ratio is not the ratio of derivatives

print(f'd(f/g):\n')
display( sym.diff(f/g) )

print(f'\n\ndf/dg:\n')
display( sym.diff(f)/sym.diff(g) )

# Exercise 4: Chain rule with two and three functions

# individual functions
f = 3*x**2
g = x**3 + sym.log(x)
h = sym.cos(x)

# composite functions
compfun2 = f.subs(x, g)
compfun3 = f.subs(x, g.subs(x, h) )

# print the 2-function composite and its derivative

print(f"f(g(x)) = \n")
display(compfun2)

print(f"\n\nf(g(x))' = \n")
display( sym.diff(compfun2) )

# print the 3-function composite and its derivative

print(f"f(g(h(x))) = \n")
display(compfun3)

print(f"\n\nf(g(h(x)))' = \n")
display( sym.diff(compfun3) )

# the plots!
sym.plot(compfun3, ylim=[0, 10], title='3-composite function')
sym.plot(sym.diff(compfun3), ylim=[-10, 10], title='Its derivative')

