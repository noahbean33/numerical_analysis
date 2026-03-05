"""Gradient Descent with AdaGrad (Adaptive Gradient) optimization."""
import numpy as np
import numpy.typing as npt


def f(x: float, y: float) -> float:
    """Cost function to minimize: f(x,y) = x^2 + y^2 + 3.
    
    Args:
        x: First variable
        y: Second variable
        
    Returns:
        Function value at (x, y)
    """
    return x * x + y * y + 3


def df(x: float, y: float) -> npt.NDArray:
    """Gradient of cost function.
    
    Args:
        x: First variable
        y: Second variable
        
    Returns:
        Gradient vector [df/dx, df/dy]
    """
    return np.asarray([2.0 * x, 2.0 * y])


def adaptive_gradient(bounds: npt.NDArray, n: int, alpha: float, epsilon: float = 1e-8) -> None:
    """Minimize function using AdaGrad optimization.
    
    AdaGrad adapts the learning rate for each parameter based on
    the history of gradients for that parameter.
    
    Args:
        bounds: Parameter bounds (not used, for compatibility)
        n: Number of iterations
        alpha: Initial learning rate
        epsilon: Small constant for numerical stability
    """
    # Initial point
    solution = np.asarray([0.7, 0.8])
    # Sum of squared gradients for each parameter
    g_sums = [0.0 for _ in range(bounds.shape[0])]

    # Optimization loop
    for _ in range(n):
        # Compute gradient
        gradient = df(solution[0], solution[1])

        # Accumulate squared gradients
        for i in range(gradient.shape[0]):
            g_sums[i] += gradient[i] ** 2.0

        # Update each parameter with adaptive learning rate
        new_solution = []

        for i in range(solution.shape[0]):
            # Adaptive learning rate: alpha / sqrt(sum of squared gradients)
            adaptive_alpha = alpha / (np.sqrt(g_sums[i]) + epsilon)
            new_solution.append(solution[i] - adaptive_alpha * gradient[i])

        solution = np.asarray(new_solution)
        solution_value = f(solution[0], solution[1])
        print('(%s) - function value: %s' % (solution, solution_value))


if __name__ == '__main__':
    adaptive_gradient(np.asarray([[-1.0, 1.0], [-1.0, 1.0]]), 200, 0.1)