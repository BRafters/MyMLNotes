import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Example dataset:
def example_dataset():
    months = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    revenue = [52, 74, 79, 95, 115, 110, 129, 126, 147, 146, 156, 184]

    return (months, revenue)

def example_dataset_two():
    temperature = np.array(range(60, 100, 2))
    sales = [65, 58, 46, 45, 44, 42, 40, 40, 36, 38, 38, 28, 30, 22, 27, 25, 25, 20, 15, 5]

    return (temperature, sales)

def real_dataset():
    df = pd.read_csv("LinearRegression/datasets/baseball_heights_weights.csv")

    X = df["height"]
    Y = df["weight"]

    return (X, Y)


# As we try to minimize "Loss", we take each parameter we are changing, and move it as long as we decrease "Loss"
# The process by which we do this is called *Gradient Descent*
# We move in the direction that decreases our loss the most
# *Gradient* refers to the slope of the curve at any point

# The following is the formula for calculating gradient of loss as intercept changes
# N = number of data points, m = current gradient guess, b = current intercept guess
# We find b with y_value - (m * x_value + b) for all x and y values we have
# Then we multiply by a factor of -2/N
def get_gradient_at_b(x_values, y_values, m, b):
    n = len(x_values)
    diff = 0

    for i in range(len(x_values)):
        x = x_values[i]
        y = y_values[i]
        diff += y - (m * x + b)

    b_gradient = -2 / n * diff

    return b_gradient

# The following is the formula to find the m gradient, or the way loss changes as the slope of our line changes
# We find m with x_value * (y_value - (m * x_value + b))
def get_gradient_at_m(x_values, y_values, m, b):
    n = len(x_values)
    diff = 0

    for i in range(len(x_values)):
        x = x_values[i]
        y = y_values[i]
        diff += x * (y - (m * x + b))
    
    m_gradient = -2 / n * diff

    return m_gradient

# Now that we know how to calculate the gradient, we want to take a step in that direction
# Ensure not to overshoot the minimum Loss
# We can scale the size of the step by multiplying the gradient by a *learning rate*
# To find a new *b* value, we would say: new_b = current_b - (learning_rate * b_gradient)
# To find a new *m* value, we would say: new_m = current_m - (learning_rate * m_gradient)
def step_gradient(x, y, m_current, b_current, learning_rate):
    b_gradient = get_gradient_at_b(x, y, m_current, b_current)
    m_gradient = get_gradient_at_m(x, y, m_current, b_current)

    b = b_current - (learning_rate * b_gradient)
    m = m_current - (learning_rate * m_gradient)

    return (m, b)

# The gradient descent algorithm
# Continuously calculates the slope and intercept to get the line of best fit, as well as to reduce loss
def gradient_descent(x, y, learning_rate, num_iterations):
    b = m = 0

    for i in range(num_iterations):
        m, b = step_gradient(x, y, m, b, learning_rate)

    return [m, b]


# m, b = gradient_descent(months, revenue, 0.01, 1000)

# calculate the line
# y = [m * x + b for x in months]
# plt.plot(months, revenue, "o")
# plt.plot(months, y)
# plt.show()

xs, ys = real_dataset()
m, b = gradient_descent(xs, ys, 0.0001, 1000)
y = [m * x + b for x in xs]
plt.plot(xs, ys, "o")
plt.plot(xs, y)
plt.show()