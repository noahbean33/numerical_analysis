"""Gradient Descent optimization algorithm for 1D functions."""
from numpy import arange
from typing import Tuple, List
import numpy as np
import numpy.typing as npt
from matplotlib import pyplot as plt


def f(x: float) -> float:
    """Cost function to minimize: f(x) = x^2.
    
    Args:
        x: Input value
        
    Returns:
        Function value at x
    """
    return x * x


def df(x: float) -> float:
    """Derivative of cost function: f'(x) = 2x.
    
    Args:
        x: Input value
        
    Returns:
        Derivative value at x
    """
    return 2 * x


def gradient_descent(start: float, end: float, n: int, alpha: float) -> Tuple[List[float], List[float]]:
    """Minimize function using gradient descent.
    
    Args:
        start: Lower bound for random initialization
        end: Upper bound for random initialization
        n: Number of iterations
        alpha: Learning rate
        
    Returns:
        Tuple of (x_values, y_values) tracking optimization path
    """
    # Track optimization path
    x_values = []
    y_values = []
    # Random initial point
    x = np.random.uniform(start, end)
    # Optimization iterations
    for i in range(n):
        # Gradient descent update: x_new = x_old - alpha * gradient
        x = x - alpha * df(x)
        # Store values
        x_values.append(x)
        y_values.append(f(x))
        print('#%d f(%s) - %s' % (i, x, f(x)))

    return x_values, y_values


if __name__ == '__main__':
    # perform the gradient descent search
    solutions, scores = gradient_descent(-1, 1, 50, 0.1)
    # sample input range uniformly at 0.1 increments to plot the function
    inputs = arange(-1, 1.1, 0.1)
    # create a line plot of input vs result
    plt.plot(inputs, f(inputs))
    # this is how we plot the steps of the algorithm
    plt.plot(solutions, scores, '.-', color='green')
    plt.show()