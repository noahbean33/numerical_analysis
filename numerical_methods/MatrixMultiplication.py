"""Matrix multiplication implementation."""
from typing import List


def multiply(a: List[List[float]], b: List[List[float]]) -> List[List[float]]:
    """Multiply two matrices: C = A * B.
    
    Args:
        a: First matrix (m x n)
        b: Second matrix (n x p)
        
    Returns:
        Result matrix C (m x p)
    """
    # Initialize result matrix with zeros
    c = [[0 for _ in range(len(b[0]))] for _ in range(len(a))]

    # Iterate through rows of A
    for i in range(len(a)):
        # Iterate through columns of B
        for j in range(len(b[0])):
            # Compute dot product
            for k in range(len(b)):
                c[i][j] += a[i][k] * b[k][j]

    return c


if __name__ == '__main__':
    print(multiply([[1, 2], [3, 4]], [[1, 2], [2, 1]]))