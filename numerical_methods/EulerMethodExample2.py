"""Euler's method for solving ODEs - Example 2: Simple pendulum."""
from matplotlib import pyplot as plt


def f(g: float, l: float, x: float) -> float:
    """Acceleration of a simple pendulum.
    
    Args:
        g: Gravitational acceleration
        l: Length of pendulum
        x: Angular displacement
        
    Returns:
        Angular acceleration
    """
    return (-g / l) * x


def euler_method(x: float = 0, v: float = 1, g: float = 9.8, l: float = 1, dt: float = 0.001) -> None:
    """Solve pendulum motion using Euler's method.
    
    Args:
        x: Initial angular displacement
        v: Initial angular velocity
        g: Gravitational acceleration
        l: Pendulum length
        dt: Time step
    """
    x_values = []
    t_values = []
    t = 0.0

    while t < 10:
        x_values.append(x)
        t_values.append(t)
        v = v + dt * f(g, l, x)
        x = x + v * dt
        t = t + dt

    plt.plot(t_values, x_values)
    plt.show()


if __name__ == '__main__':
    euler_method()
