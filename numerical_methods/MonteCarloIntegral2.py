"""Monte Carlo integration using expected value method."""
import numpy as np


def f(x: float) -> float:
    """Example function to integrate: f(x) = x^3.
    
    Args:
        x: Input value
        
    Returns:
        Function value at x
    """
    return x * x * x


class MonteCarloIntegration:
    """Monte Carlo integration using expected value method.
    
    This approach estimates the integral by averaging function
    values at random points.
    """

    def __init__(self, a: float, b: float, n: int = 100):
        """Initialize Monte Carlo integration.
        
        Args:
            a: Lower bound
            b: Upper bound
            n: Number of random samples
        """
        self.a = a
        self.b = b
        self.n = n

    def run(self) -> float:
        """Run Monte Carlo integration using expected value.
        
        Returns:
            Approximate value of the integral
        """
        # Sum of function values
        s = 0.0

        for _ in range(self.n):
            random_x = self.generate_random()
            s += f(random_x) * (self.b - self.a)

        return s / self.n

    def generate_random(self) -> float:
        """Generate random float in [a, b].
        
        Returns:
            Random value in the interval
        """
        return self.a + (self.b - self.a) * np.random.uniform()


if __name__ == '__main__':
    algorithm = MonteCarloIntegration(0, 5, 10000000)
    print(algorithm.run())
