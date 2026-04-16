import matplotlib.pyplot as plt

"""
For our program to make a level of guess, we have to determine what a line would look like through these data points
"""

# A Line is determined by its slope (m) and intercept (b)
# Slope is how steep a line is
# Intercept is where the line hits the y-axis
# For each point, we can say y = mx + b

months = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
revenue = [52, 74, 79, 95, 115, 110, 129, 126, 147, 146, 156, 184]

m = 11
b = 47

plt.plot(months, revenue, "o")

# Using list comprehension to create a list of points to make into a line
y = [m * x + b for x in months]
plt.plot(months, y)
plt.show()