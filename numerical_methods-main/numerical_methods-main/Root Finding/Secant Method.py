import math

def f(x):
    p = 3 * pow(2, -18)
    q = 2
    return (pow(x, 3) - p * x - q)

def secant(y,x,tol):
    maxit = 200;
    r = 1.25992407762209935560844934660
    n = 0
    error = abs(x - r)
    resid = abs(f(x))

    while (error > tol) and (n <= maxit) and (f(x) != f(y)):
        z = x
        x = (y * f(x) - x * f(y))/(f(x) - f(y))
        y = z

        resid = abs(f(x))
        error = abs(x - r)
        n = n + 1

        print('n = ', n, '   ', 'x = ', x, '   ', '|x - r| = ', error,'   ', '|f(x)| = ', resid,'   ', 'x - prev_x = ', x-z)

    if (n >= maxit):
        print('Max iterations reached')
    elif (f(x) - f(y) < pow(2, -52)):
        print('f(x) = f(y) on the order of machine epsilon so process terminated')
    else:
        print('The final results are: ')
        print('n = ', n, 'x = ', x, 'f(x) = ', f(x))

secant(1, 2, pow(2,-52))


