"""Inner product (dot product) of vectors."""
from typing import List


def multiply(a: List[float], b: List[float]) -> float:
    """Compute inner product of two vectors (iterative).
    
    Args:
        a: First vector
        b: Second vector
        
    Returns:
        Inner product (scalar)
    """
    c = 0.0

    for i in range(len(a)):
        c += a[i] * b[i]

    return c


def multiply_python(a: List[float], b: List[float]) -> float:
    """Compute inner product using Python built-ins.
    
    Args:
        a: First vector
        b: Second vector
        
    Returns:
        Inner product (scalar)
    """
    return sum([i * j for (i, j) in zip(a, b)])


if __name__ == '__main__':
    print(multiply([1, 2, 4, 5], [2, 5, 4, 5]))
    print(multiply_python([1, 2, 4, 5], [2, 5, 4, 5]))