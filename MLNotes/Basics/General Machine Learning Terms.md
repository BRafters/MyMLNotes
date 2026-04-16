**Supervised Learning**: Data is labeled. The program learns to predict the output from the input data
**Unsupervised Learning**: Data is unlabeled. The program learns to recognize the inherent structure in the input data

### What is a Feature?

A feature in Machine Learning refers to a measurable property or characteristic of a phenomenon being observed.

Features are the input variables that the model uses to make predictions
- They are also known as
    - Independent Variables
    - Predictors
    - Attributes
- Features are also known as **Independent Variables**. They are not directly caused by the label
### Characteristics of Features

1. **Measurable**
    - Features are quantifiable properties that can be measured and recorded
2. **Independent**
    - Each feature should ideally be independent of the others, providing unique information to the model
3. **Varied Types**
    - Features can be numerical (e.g., age, height), categorical (e.g., gender, color), or even text-based (e.g., reviews, comments)

##### Examples of Features

- In a dataset predicting house prices, features might include the number of bedrooms, square footage, and location
- For a spam email filter classifier, features could be the presence of certain keywords, the length of the email, and the senders address

### What is a Label? 

A label, AKA the **target variable** or **dependent variable**. It is the output that the model is trained to predict.
- In other words, the **dependent variable** depends on the features

Labels are the “answer” you want the model to learn to generate from the features.

In **supervised learning**, labels are the known outcomes that the model learns to associate with the input features during training
##### Characteristics of Labels

1. Dependent
    1. Labels depend on the input features and are the result of the models prediction
2. Categorical or Numerical
    1. Labels can be categorical  (e.g., spam or not spam) or numerical (e.g., price of a house)
##### Examples of Labels

- In a house price prediction model, the label would be the actual price of the house
- For a spam email classifier, the label would be whether the email is spam or not

They are only used during training (and evaluation). Once the model is trained, it can predict labels for new, unseen data using just features
##### What is a Classifier?

- A Classifier is an algorithm that organizes data into one or more classes based on certain characteristics
