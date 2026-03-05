"""Matrix-vector multiplication."""
from typing import List


def multiply(a: List[List[float]], b: List[float]) -> List[float]:
    """Multiply matrix by vector: c = A * b.
    
    Args:
        a: Matrix A (m x n)
        b: Vector b (n)
        
    Returns:
        Result vector c (m)
    """
    # Initialize result vector
    c = [0.0 for _ in range(len(a))]

    # Iterate through rows of matrix
    for i in range(len(a)):
        # Compute dot product with vector
        for j in range(len(b)):
            c[i] += a[i][j] * b[j]

    return c


if __name__ == '__main__':
    print(multiply([[3, 2, 0], [0, 4, 1], [2, 0, 1]], [4, 3, 1]))