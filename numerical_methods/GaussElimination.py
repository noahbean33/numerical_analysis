"""Gaussian elimination for solving systems of linear equations."""
import numpy as np
import numpy.typing as npt


def gaussian_elimination(a: npt.NDArray, b: npt.NDArray) -> npt.NDArray:
    """Solve Ax = b using Gaussian elimination with back substitution.
    
    Args:
        a: Coefficient matrix A (modified in-place)
        b: Right-hand side vector (modified in-place, becomes solution)
        
    Returns:
        Solution vector x
    """
    n = len(b)
    # Forward elimination: make matrix upper triangular
    for k in range(n - 1):
        # Eliminate values below pivot
        for i in range(k + 1, n):
            if a[i, k] != 0.0:
                # Compute multiplier
                lam = a[i, k] / a[k, k]
                # Row operation: row_i = row_i - lam * row_k
                a[i, k:n] = a[i, k:n] - lam * a[k, k:n]
                b[i] = b[i] - lam * b[k]

    # Back substitution
    for k in range(n - 1, -1, -1):
        b[k] = (b[k] - np.dot(a[k, k + 1:n], b[k + 1:n])) / a[k, k]

    return b


if __name__ == '__main__':
    print(gaussian_elimination(np.array([[1., 1.], [0.035, 0.05]]), np.array([24000., 930.])))


