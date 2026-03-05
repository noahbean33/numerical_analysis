"""Monte Carlo integration using hit-or-miss method."""
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
    """Monte Carlo integration using hit-or-miss method.
    
    Generates random points in a bounding box and counts
    how many fall below the function curve.
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
        """Run Monte Carlo integration.
        
        Returns:
            Approximate value of the integral
        """
        # Count points under f(x)
        counter = 0

        for _ in range(self.n):
            random_x = self.generate_random()
            random_y = self.generate_random()

            if self.is_below(random_x, random_y):
                counter += 1

        return self.get_total_area() * counter / self.n

    def get_total_area(self) -> float:
        """Calculate bounding box area.
        
        Note: Requires knowing function bounds (main limitation).
        
        Returns:
            Area of the bounding box
        """
        return (self.b - self.a) * (self.b - self.a)

    def generate_random(self) -> float:
        """Generate random float in [a, b].
        
        Returns:
            Random value in the interval
        """
        return self.a + (self.b - self.a) * np.random.uniform()

    @staticmethod
    def is_below(x: float, y: float) -> bool:
        """Check if point (x, y) is below f(x).
        
        Args:
            x: x-coordinate
            y: y-coordinate
            
        Returns:
            True if y < f(x)
        """
        return y < f(x)


if __name__ == '__main__':
    algorithm = MonteCarloIntegration(0, 5, 1000000)
    print(algorithm.run())
