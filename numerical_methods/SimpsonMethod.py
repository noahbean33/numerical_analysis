"""Numerical integration using Simpson's rule."""


def f(x: float) -> float:
    """Example function to integrate: f(x) = x^2.
    
    Args:
        x: Input value
        
    Returns:
        Function value at x
    """
    return x * x


def integral(a: float, b: float, n: int = 1000) -> float:
    """Compute definite integral using Simpson's rule.
    
    Args:
        a: Lower bound of integration
        b: Upper bound of integration
        n: Number of subintervals (should be even)
        
    Returns:
        Approximate value of the integral
    """
    h = (b - a) / n
    s = 0.0

    # Evaluate at boundaries
    s += f(a) + f(b)

    # Odd indices get coefficient 4
    for i in range(1, n, 2):
        s += 4 * f(a + i * h)

    # Even indices get coefficient 2
    for i in range(2, n, 2):
        s += 2 * f(a + i * h)

    return h * s / 3


if __name__ == '__main__':
    print(integral(0, 1))

