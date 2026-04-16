from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import pandas as pd

# Grab our data
df = pd.read_csv("MultipleLinearRegression/datasets/manhattan.csv")

print(df.head())

# Create our *x* axis
x = df [['bedrooms', 'bathrooms', 'size_sqft', 'min_to_subway', 'floor',
'building_age_yrs', 'no_fee', 'has_roofdeck', 'has_washer_dryer', 'has_doorman', 
'has_elevator','has_dishwasher', 'has_patio', 'has_gym']]

# Create our *y* axis
y = df[['rent']]

# Split between training set and test set for each axis
x_train, x_test, y_train, y_test = train_test_split(x, y, train_size=0.8, test_size=0.2, random_state=6)

# The steps for multiple linear regression are identical to the steps for simple linear regression
mlr = LinearRegression()

# Fit using our training dataset
model = mlr.fit(x_train, y_train)

# We can also use the .predict() function to pass in x-values. It returns y-values that this plane would predict.
y_predict = mlr.predict(x_test)
print(model.coef_)

# Look at the test data, compared to the projection
plt.scatter(y_test, y_predict, alpha=0.4)
plt.xlabel("Prices")
plt.ylabel("Predicted Prices")
plt.title("Cost of rent vs. Predicted cost of rent")
plt.show()