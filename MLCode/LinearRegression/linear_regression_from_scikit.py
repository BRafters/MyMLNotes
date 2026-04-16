from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import numpy as np

def example_dataset():
    months = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    revenue = [52, 74, 79, 95, 115, 110, 129, 126, 147, 146, 156, 184]

    return (months, revenue)

def example_dataset_two():
    temperature = np.array(range(60, 100, 2))
    temperature = temperature.reshape(-1, 1)
    sales = [65, 58, 46, 45, 44, 42, 40, 40, 36, 38, 38, 28, 30, 22, 27, 25, 25, 20, 15, 5]

    return (temperature, sales)

x, y = example_dataset_two()

# We first fit the linear regression model to our data using:
line_fitter = LinearRegression()
line_fitter.fit(x, y)

# .fit() gives us two variables that are useful to us
m = line_fitter.coef_ # The slope
b = line_fitter.intercept_ # The intercept

# We can also use the .predict() function to pass in x-values and receive y-values that this line would predict
# *num_iterations and learning_rate have default values in scikit-learn
y_predicted = line_fitter.predict(x)

print(line_fitter.get_params(True))

plt.plot(x, y, "o")
plt.plot(x, y_predicted)
plt.show()