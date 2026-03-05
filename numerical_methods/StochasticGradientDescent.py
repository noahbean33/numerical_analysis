"""Stochastic Gradient Descent (SGD) for linear regression.

Batch size variants:
- batch_size = number of samples: Batch gradient descent
- batch_size = 1: True stochastic gradient descent  
- batch_size = [2, n]: Mini-batch gradient descent
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error
from typing import Tuple


def sgd(x_values: pd.Series, y_values: pd.Series, alpha: float = 0.01, 
        epoch: int = 20, batch_size: int = 3) -> Tuple[float, float, list]:
    """Train linear regression model using SGD.
    
    Args:
        x_values: Training features
        y_values: Training targets
        alpha: Learning rate
        epoch: Number of training epochs
        batch_size: Number of samples per batch
        
    Returns:
        Tuple of (slope, intercept, mse_history)
    """
    # Initialize model parameters
    m, b = 0.5, 0.5
    # Track MSE over epochs
    error = []

    for _ in range(epoch):
        # Random mini-batch sampling
        indexes = np.random.randint(0, len(x_values), batch_size)

        xs = np.take(x_values, indexes)
        ys = np.take(y_values, indexes)
        n = len(xs)

        # Prediction error
        f = (b + m * xs) - ys

        # Gradient descent updates
        m += -alpha * 2 * xs.dot(f).sum() / n
        b += -alpha * 2 * f.sum() / n

        # Track error on full dataset
        error.append(mean_squared_error(y_values, b + m * x_values))

    return m, b, error


def plot_regression(x_values: pd.Series, y_values: pd.Series, y_predictions: pd.Series) -> None:
    """Plot regression line and data points.
    
    Args:
        x_values: Feature values
        y_values: True target values
        y_predictions: Predicted values
    """
    plt.figure(figsize=(8, 6))
    plt.title('Regression with Stochastic Gradient Descent (SGD)')
    plt.scatter(x_values, y_values, label='Data Points')
    plt.plot(x_values, y_predictions, c='#FFA35B', label='Regression')
    plt.legend(fontsize=10)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()


def plot_mse(mse_values: list) -> None:
    """Plot MSE over epochs.
    
    Args:
        mse_values: List of MSE values per epoch
    """
    plt.figure(figsize=(8, 6))
    plt.plot(range(len(mse_values)), mse_values)
    plt.title('Stochastic Gradient Descent Error')
    plt.xlabel('Epochs')
    plt.ylabel('MSE')
    plt.show()


if __name__ == '__main__':
    x = pd.Series([1, 2, 3, 5, 6, 7, 8])
    y = pd.Series([1, 2, 3, 5, 6, 7, 8])
    slope, intercept, mses = sgd(x, y, alpha=0.01, epoch=1000, batch_size=3)
    # the model is the linear regression model
    model_predictions = intercept + slope * x

    # show the results
    print('Slope and intercept: %s - %s' % (slope, intercept))
    print('MSE: %s' % mean_squared_error(y, model_predictions))
    plot_regression(x, y, model_predictions)
    plot_mse(mses)