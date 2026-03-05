"""Euler's method for solving ODEs - Example 1: dy/dx = cos(x)."""
import numpy as np
from matplotlib import pyplot as plt


def f(x: float, y: float) -> float:
    """ODE: dy/dx = cos(x), exact solution: y = sin(x).
    
    Args:
        x: Independent variable
        y: Dependent variable
        
    Returns:
        Derivative dy/dx at (x, y)
    """
    return np.cos(x)


def euler_method(x: float = 0, y: float = 1, h: float = 0.01) -> None:
    """Solve ODE using Euler's method.
    
    Initial condition: y(0) = 1
    
    Args:
        x: Initial x value
        y: Initial y value
        h: Step size
    """
    x_values = []
    y_values = []

    while x < 10:
        x_values.append(x)
        y_values.append(y)
        y = y + h * f(x, y)
        x = x + h

    plt.plot(x_values, y_values)
    plt.show()


if __name__ == '__main__':
    euler_method()
