from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

regr = LinearRegression()
year_col_name = "year"
totalprod_col_name = "totalprod"

df = pd.read_csv("LinearRegression/datasets/honey_production.csv")

# Using .groupby() to get the mean of totalprod per year
prod_per_year = df.groupby(year_col_name).totalprod.mean().reset_index()

# Creating X that is the column of years. Needs to be reshaped to be in correct format
X = prod_per_year[year_col_name]
X = X.values.reshape(-1, 1)
y = prod_per_year[totalprod_col_name]

# Fit the data against the model
regr.fit(X, y)

# Predictions to make using the X data
y_predict = regr.predict(X)

# Creating a range from 2013 to 2050
X_future = np.array(range(2013, 2050))
X_future = X_future.reshape(-1, 1)

# Running a prediction against the future using the data we've fit to the model
future_predict = regr.predict(X_future)

plt.scatter(X, y)
plt.plot(X, y_predict)
plt.plot(X_future, future_predict)
plt.show()