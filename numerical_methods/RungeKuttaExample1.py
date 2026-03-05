"""Runge-Kutta 4th order method - Example 1: Damped pendulum."""
import numpy as np
from matplotlib import pyplot as plt


def f(g: float, l: float, x: float, b: float, v: float) -> float:
    """Acceleration of a damped pendulum.
    
    Args:
        g: Gravitational acceleration
        l: Length of pendulum
        x: Angular displacement
        b: Damping coefficient
        v: Angular velocity
        
    Returns:
        Angular acceleration
    """
    return (-g / l) * x - b * v


def runge_kutta_method(x: float = 0, v: float = 1, g: float = 0.98, l: float = 1, 
                        dt: float = 0.1, b: float = 0.3) -> None:
    """Solve damped pendulum using Runge-Kutta 4th order method.
    
    Args:
        x: Initial angular displacement
        v: Initial angular velocity
        g: Gravitational acceleration
        l: Pendulum length
        dt: Time step
        b: Damping coefficient
    """
    x_values = []
    t_values = []
    t = 0.0

    while t < 100:
        x_values.append(x)
        t_values.append(t)

        k1 = dt * f(g, l, x, b, v)
        k2 = dt * f(g, l, x, b, v + dt * k1 / 2)
        k3 = dt * f(g, l, x, b, v + dt * k2 / 2)
        k4 = dt * f(g, l, x, b, v + dt * k3)

        v = v + 1.0 / 6.0 * (k1 + 2 * k2 + 2 * k3 + k4)
        x = x + v * dt
        # BUG FIX: Missing time increment
        t = t + dt

    plt.plot(t_values, x_values)
    plt.show()


if __name__ == '__main__':
    runge_kutta_method()
