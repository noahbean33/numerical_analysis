"""Lagrange interpolation using least squares polynomial fitting."""
import numpy as np
import matplotlib.pyplot as plt
from typing import List, Optional
import numpy.typing as npt


class LagrangeInterpolation:
    """Polynomial interpolation using least squares method.
    
    Fits a polynomial of degree n to data points using Gaussian elimination.
    """

    def __init__(self, x: List[float], y: List[float], n: int):
        """Initialize interpolation.
        
        Args:
            x: x-coordinates of data points
            y: y-coordinates of data points
            n: Degree of polynomial
        """
        self.x = x
        self.y = y
        self.n = n
        self.b: Optional[npt.NDArray] = None
        self.m = [[0 for _ in range(n + 1)] for _ in range(len(x))]

    def plot(self) -> None:
        """Plot data points and fitted polynomial."""
        plt.scatter(self.x, self.y)

        x = np.linspace(-3, 3, 100)
        fx = 0

        # Evaluate polynomial
        for i in range(len(self.b)):
            fx += self.b[i] * x ** i

        plt.plot(x, fx)
        plt.show()

    def solve(self) -> None:
        """Solve for polynomial coefficients using least squares."""
        # Set matrix first column to 1 (constant term)
        for i in range(len(self.x)):
            self.m[i][0] = 1

        # Other columns are powers of x
        for i in range(1, self.n + 1):
            for j in range(len(self.x)):
                self.m[j][i] = pow(self.x[j], i)

        # Build normal equations: M^T * M * b = M^T * y
        self.m = np.array(self.m)
        self.b = self.m.transpose().dot(self.y)
        self.m = np.matmul(self.m.transpose(), self.m)

        # Solve using Gaussian elimination
        self.gaussian_elimination()
        print('Result of interpolation: %s' % self.b)

    def gaussian_elimination(self) -> None:
        """Solve linear system using Gaussian elimination."""
        n = len(self.b)
        # Forward elimination
        for k in range(n - 1):
            # Eliminate below pivot
            for i in range(k + 1, n):
                if self.m[i, k] != 0.0:
                    # Compute multiplier
                    lam = self.m[i, k] / self.m[k, k]
                    # Row operation
                    self.m[i, k:n] = self.m[i, k:n] - lam * self.m[k, k:n]
                    self.b[i] = self.b[i] - lam * self.b[k]

        # Back substitution
        for k in range(n - 1, -1, -1):
            self.b[k] = (self.b[k] - np.dot(self.m[k, k + 1:n], self.b[k + 1:n])) / self.m[k, k]


if __name__ == '__main__':
    algorithm = LagrangeInterpolation([-2, -1, 0, 1, 2], [5.1, 1.9, 1.1, 2.1, 4.9], 2)
    algorithm.solve()
    algorithm.plot()

