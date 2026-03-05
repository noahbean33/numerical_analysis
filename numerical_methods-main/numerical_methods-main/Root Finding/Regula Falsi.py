# define function with potential roots we are searching for
import math

def f(x):
    return(((1/2) * abs(pow(x,3/2)) - x)/((1/2) * abs(pow(x,3/2)) + 1))

# Define Regula Falsi Function
def regulaf(a, b):
    # declare max iterations, tolerance, f(a) and f(b)
    nmax = 10000
    tol = pow(2,-52)
    fa = f(a)
    fb = f(b)

    # if interval does not have change of sign, no root, not viable
    if fa * fb >= 0:
        print('Bad search interval.')
        x = 'NaN'
        fx = 'NaN'
        n = 0

    # if good search interval, x is midpoint,
    # initialize n, fx
    else:
        x = (a * f(b) - b * f(a))/(f(b) - f(a))
        fx = f(x)
        n = 0

        # while less than max iterations and greater than tolerance,
        # run regula falsi method algorithm
        while ((n <= nmax) and ((x-0) > tol)):
            if fx * fa < 0:
                b = x
                fb = fx
            else:
                a = x
                fa = fx
            z = x
            x = (a * f(b) - b * f(a))/(f(b) - f(a))
            fx = f(x)
            n = n + 1
            print('n = ', n, '   ', 'x = ', "{:e}".format(x),
                  '   ','f(x) = ', "{:e}".format(fx), '   ', 'x(n+1)/[x(n)] = ', "{:e}".format(x/pow(z,1)))

    # print n,x,f(x)
    print()
    print('The final root approx. info: ')
    print('n = ', n, 'x = ', x, 'f(x) = ', fx)

regulaf(-1,1)


