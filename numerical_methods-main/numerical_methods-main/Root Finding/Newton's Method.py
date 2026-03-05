import math

def f(x):
    #p = 3 * pow(2,-18)
    #q = 2
    #return (pow(x,3) - p * x - q)
    return (pow(x, 3) - 2 * x + 2)

def fp(x):
    p = 3 * pow(2, -18)
    #return (3*pow(x,2) - p)
    return (3*pow(x,2) - 2)

def newton(x,tol):
    maxit = 100
    #r = 1.25992407762209935560844934660
    r = -1.769292354238631
    n = 0
    #p = 3 * pow(2, -18)
    #q = 2
    error = abs(x - r)
    resid = abs(f(x))

    while (error > tol) and (n <= maxit):
        xprev = x
        #x = (2 * pow(x,3) + q)/(3 * pow(x,2) - p)
        x = x - (f(x)/fp(x))
        error = abs(x - r)
        resid = abs(f(x))

        n = n + 1
        #print('n = ', n, '   ', 'x = ', x, '   ', '|x - r| = ', error, '   ', 'f(x) = ', f(x))
        print('n = ', n, '   ', 'x = ', x, '   ', '|x - r| = ', error, '   ', 'x - prev_x = ', x-xprev, '   ', '|f(x)| = ', resid)


    if (n >= maxit):
        print('Max iterations reached')

    else:
        print('The final results are: ')
        print('n = ', n, 'x = ', x, 'f(x) = ', f(x))

#newton(1, pow(2,-52))
newton(0.2, pow(2,-52))


