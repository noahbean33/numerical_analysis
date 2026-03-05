"""Newton-Raphson method for finding roots of equations."""
from math import sqrt


def f(x: float) -> float:
    """Example function: f(x) = x^2 - 2.
    
    Args:
        x: Input value
        
    Returns:
        Function value at x
    """
    return x * x - 2


def df(x: float) -> float:
    """Derivative of f(x): f'(x) = 2x.
    
    Args:
        x: Input value
        
    Returns:
        Derivative value at x
    """
    return 2 * x


def newton_method(x: float, n: int = 10) -> float:
    """Find root using Newton-Raphson method.
    
    Args:
        x: Initial guess
        n: Number of iterations
        
    Returns:
        Approximate root of the function
    """
    counter = 0

    while counter < n:
        counter += 1
        x = x - f(x) / df(x)

    return x


if __name__ == '__main__':
    print(newton_method(1))
    print(sqrt(2))

