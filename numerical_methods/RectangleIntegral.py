"""Numerical integration using rectangle (midpoint) rule."""


def f(x: float) -> float:
    """Example function to integrate: f(x) = x^2.
    
    Args:
        x: Input value
        
    Returns:
        Function value at x
    """
    return x * x


def rectangle_integral(a: float, b: float, n: int = 1000000) -> float:
    """Compute definite integral using rectangle rule.
    
    Args:
        a: Lower bound of integration
        b: Upper bound of integration
        n: Number of rectangles
        
    Returns:
        Approximate value of the integral
    """
    # Width of a single rectangle
    h = (b - a) / n
    # Sum of areas
    s = 0.0

    # Sum up the areas of all rectangles
    for i in range(n):
        s += h * f(a + i * h)

    return s


if __name__ == '__main__':
    print(rectangle_integral(0, 1))

