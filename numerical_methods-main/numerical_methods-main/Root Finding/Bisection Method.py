# define function with potential roots we are looking for 
import math


def f(x):
    return (x - math.tan(x))

# Define Bisection Function
def bisection(a, b):
    # declare max iterations, tolerance, f(a) and f(b)
    nmax = 200
    tol = (pow(10,-8))/2
    fa = f(a)
    fb = f(b)

    # if interval does not have change of sign, no root, not viable
    if fa * fb >= 0:
        print('Bad search interval.')
        x = 'NaN'
        fx = 'NaN'
        n = 0
        d = 'Nan'

    # if good search interval, x is midpoint,
    # initialize n, fx, and error bound d = (b-a)/2
    else:
        x = (a + b) / 2
        fx = f(x)
        n = 0
        d = (b - a) / 2

        # while less than max iterations and greater than tolerance,
        # run bisection method algorithm
        while ((n <= nmax) and (abs(fx) > tol) and (d > tol)):
            if fx * fa < 0:
                b = x
                fb = fx
            else:
                a = x
                fa = fx

            x = (a + b) / 2
            fx = f(x)
            n = n + 1
            d = d / 2
            #print('n = ', n, 'x = ', x, 'f(x) = ', fx, 'd = ', d)

    # print n,x,f(x),d
    print('n = ', n, 'x = ', x, 'f(x) = ', fx, 'd = ', d)

bisection(-4.5,-4)


