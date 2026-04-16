Regression vs. Classification

### Regression

- Is used to predict outputs that are continuous
- Outputs are quantities that can be flexibly determined based on the inputs of the model rather than being confined to a set of possible labels
- **Linear Regression** is the most popular regression algorithm
    - Often underrated because of it’s relative simplicity
    - Could be used to predict the likelihood that a customer will churn or the revenue a customer will generate
##### Examples:

- Predict the height of a potted plant from the amount of rainfall
- Predict salary based on someones age and availability of high-speed internet
- Predict a cars MPG, based on size and model year
##### Classification

- Is used to predict a discrete label
- Outputs fall under a finite set of possible outcomes
    - Many situations have only two possible outcomes. This is called **Binary Classification**. (True/False, 0 or 1, hotdog or not hotdog)
- There’s other two common types of classification: **multi-class classification** and **multi-label classification**
    - **Multi-class classification** has the same idea behind binary classification, except instead of two possible outcomes, there are three or more
    - For example
        - Predict whether a photo contains a pear, apple, or peach
        - Predict what letter of the alphabet a handwritten character is 
        - Predict whether a piece of fruit is small, medium, or large
- An important note note about both binary classification and multi-class classification is that in both, each outcome has one specific label
- In **multi-label classification** there are multiple possible labels for each outcome
    - Useful for customer segmentation, image classifications, and sentiment analysis for understanding text
    - For example
        - Here a cat and a bird are both identified in a photo showing a classification model with more than one label as a result￼
![[Multi-label Classification.png]]
##### Examples:

- Predict whether an email is spam or not
- Predict whether it will rain or not
- Predict whether a user or is a power user or a casual user

