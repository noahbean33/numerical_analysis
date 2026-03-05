"""Numerical integration using trapezoidal rule."""


def f(x: float) -> float:
    """Example function to integrate: f(x) = x^2.
    
    Args:
        x: Input value
        
    Returns:
        Function value at x
    """
    return x * x


def integral(a: float, b: float, n: int = 10000) -> float:
    """Compute definite integral using trapezoidal rule.
    
    Args:
        a: Lower bound of integration
        b: Upper bound of integration
        n: Number of trapezoids
        
    Returns:
        Approximate value of the integral
    """
    # Width of a single trapezoid
    h = (b - a) / n
    # Sum of the areas of trapezoids
    s = 0.0

    # Evaluate function at left boundary
    s += f(a)

    # Consider internal points (weighted by 2)
    for i in range(1, n):
        s += 2 * f(a + i * h)

    # Evaluate function at right boundary
    s += f(b)

    return h * s / 2


if __name__ == '__main__':
    print(integral(0, 1))

