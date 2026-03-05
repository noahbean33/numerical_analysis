"""ADAM (Adaptive Moment Estimation) optimization algorithm."""
import numpy as np
import numpy.typing as npt


def f(x: float, y: float) -> float:
    """Cost function to minimize: f(x,y) = x^2 + y^2.
    
    Args:
        x: First variable
        y: Second variable
        
    Returns:
        Function value at (x, y)
    """
    return x * x + y * y


def df(x: float, y: float) -> npt.NDArray:
    """Gradient of cost function.
    
    Args:
        x: First variable
        y: Second variable
        
    Returns:
        Gradient vector [df/dx, df/dy]
    """
    return np.asarray([2.0 * x, 2.0 * y])


def adam(bounds: npt.NDArray, n: int, alpha: float, beta1: float, beta2: float, epsilon: float = 1e-8) -> None:
    """Minimize function using ADAM optimization.
    
    ADAM combines ideas from RMSprop and momentum:
    - Computes adaptive learning rates for each parameter
    - Maintains exponentially decaying averages of past gradients (momentum)
    - Maintains exponentially decaying averages of past squared gradients
    
    Args:
        bounds: Parameter bounds (not used, for compatibility)
        n: Number of iterations
        alpha: Learning rate (step size)
        beta1: Exponential decay rate for first moment (typically 0.9)
        beta2: Exponential decay rate for second moment (typically 0.999)
        epsilon: Small constant for numerical stability
    """
    # Initial point
    x = np.asarray([0.8, 0.9])
    # First moment (mean of gradients)
    m = [0.0 for _ in range(bounds.shape[0])]
    # Second moment (uncentered variance of gradients)
    v = [0.0 for _ in range(bounds.shape[0])]

    for t in range(1, n + 1):
        # Compute gradient
        g = df(x[0], x[1])
        # Update each parameter
        for i in range(x.shape[0]):
            # Update biased first moment estimate
            m[i] = beta1 * m[i] + (1.0 - beta1) * g[i]
            # Update biased second moment estimate
            v[i] = beta2 * v[i] + (1.0 - beta2) * g[i] ** 2
            # Bias-corrected first moment
            m_corrected = m[i] / (1.0 - beta1 ** t)
            # Bias-corrected second moment
            v_corrected = v[i] / (1.0 - beta2 ** t)
            # Update parameter
            x[i] = x[i] - alpha * m_corrected / (np.sqrt(v_corrected) + epsilon)

        print('(%s) - function value: %s' % (x, f(x[0], x[1])))


if __name__ == '__main__':
    adam(np.asarray([[-1.0, 1.0], [-1.0, 1.0]]), 100, 0.05, 0.9, 0.999)
