import pandas as pd

df = pd.read_csv("MultipleLinearRegression/datasets/queens.csv")

print(df.head())

x = df [['bedrooms', 'bathrooms', 'size_sqft', 'min_to_subway', 'floor',
'building_age_yrs', 'no_fee', 'has_roofdeck', 'has_washer_dryer', 'has_doorman', 
'has_elevator','has_dishwasher', 'has_patio', 'has_gym']]

y = df[['rent']]

# Select row 3
row_3 = df.iloc[3]
print("Distance from subway in minutes:", row_3["min_to_subway"])
print("Neighborhood:", row_3["neighborhood"])