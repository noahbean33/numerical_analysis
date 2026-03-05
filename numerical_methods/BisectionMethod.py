"""Bisection method for finding roots of equations."""
from math import sqrt


def f(x: float) -> float:
    """Example function: f(x) = x^2 - 2.
    
    Args:
        x: Input value
        
    Returns:
        Function value at x
    """
    return x * x - 2


def bisection_method(x_neg: float, x_pos: float, eps: float = 1e-10) -> float:
    """Find root using bisection method.
    
    Args:
        x_neg: Left boundary (should give f(x_neg) < 0)
        x_pos: Right boundary (should give f(x_pos) > 0)
        eps: Tolerance for convergence
        
    Returns:
        Approximate root of the function
    """
    x = 0.0

    while abs(x_pos - x_neg) > eps:
        x = (x_pos + x_neg) / 2

        if f(x) > 0:
            x_pos = x
        else:
            x_neg = x

    return x


if __name__ == '__main__':
    print(bisection_method(-2, 2))
    print(sqrt(2))
