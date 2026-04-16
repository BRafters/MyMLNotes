### The Process

When people think of machine learning, they often think of a program that is taking in data and spitting out predictions and insights. The process of Machine Learning often requires many more steps before and after the predictive analytics.
##### We try to think of the Machine Learning process as:

1. Formulating a Question
    - What is it that we want to find out? How will we reach the success criteria that we set?
    - For example: We are performing machine learning for a high-traffic casual restaurant chain and our goal is to improve the customer experience. We can serve this goal in many ways:
        - When we think about creating a model, we have to narrow down to one measurable, **specific task**
        - We might say we want to predict the wait times for food orders within 2 minutes, so that we can give them an accurate time estimate
2. Finding and Understanding the Data
    - The largest chunk of time in any machine learning process is finding the relevant data to help answer your question. As well as getting it into the format necessary for performing predictive analysis
    - We know that for **supervised learning**, we need labelled datasets, or datasets that have clear labels of what their ground truth is 
        - For the restaurant wait time, this would mean we would need many examples of past orders, tagged with how long the wait time is
        - The restaurant may already track this data, but we might need to augment the data collection with a timer that starts when the customer orders, stops when the customer receives their food, and records that information
    - Creating the system of recording data, as well as gathering enough data to be able to train our model would take time
    - Once you gathered your data, you want to understand it, so you know what model to apply and what the outputs will mean
    - First, you want to examine the statistics
        - Calculate means and medians to understand the distribution
        - Calculate percentiles
        - Find correlations that indicate relationships
    - You may also want to visualize the data, perhaps using box plots to identify outliers, histograms to show the basic structure of the data, and scatter plots to examine relationships between variables
3. Cleaning the Data and Feature Engineering
    - Real world data is messy
    - Data may have errors
    - Some columns may be empty
    - The features we’re interested in might require string manipulation to extract

    - **Cleaning the data** refers to the process by which we address missing values and outliers, among other things that may affect our insights
    - For our example, we may see a group of orders that took over 20 minutes, due to an emergency in the kitchen one afternoon
        - This can skew our predictions
        - If we want to model the more general functioning of the restaurant, we may want to remove these values

    - Feature Engineering
        - Refers to the process by which we choose the important features (or columns) to look at
        - We make the appropriate transformations to prepare our data for our model
        - We might try:
            - Normalizing or standardizing the data
            - Augmenting the data by adding new columns
            - Removing unnecessary columns

    - Normalization
        - A data preprocessing technique
        - Used to adjust the scale of numeric data features so they fall within a particular range or follow a specific distribution
        - Normalizing data helps create uniformity across features
        - It transforms values in a dataset into a common scale, which ensures that no single feature dominates others due to its magnitude
        - Without normalization machine learning algorithms can become biased toward features with larger values, resulting in skewed predictions or inefficient training
    - After we test our model on the data we have, we might go back and reengineer features to see if we get a better result
4. Choosing a Model
    - Once we understand our dataset and the problem we’re trying to solve, we can begin to choose a model that will help us tackle our problem
        - If we want to find a continuous output, like predicting the number of minutes someone should wait for their order, we should use a regression algorithm
        - If we want to classify an input, like determining if an order will take under 5 minutes or over 10 minutes, then we would use a classification algorithm
    - We use different models on categorical and numerical data
        - Then use different models on datasets with many features
        - Then different models on datasets with few features
5. Tuning and Evaluating
    - We often want to set a metric of success, so that we know the model we’ve chosen is good enough:
        - Are we looking for accuracy?
        - Are we looking for precision?
        - A combination of the two?
    - Each model has a variety of parameters that change how it makes decisions
        - We can adjust these and compare the chosen evaluation metrics of the different variants to find the most accurate model
6. Using the Model and Presenting Results
    - When you achieve the level of accuracy you want on your training set, you can use the model on the data you actually care about analyzing
    - For the restaurant example we can now start inputting orders. The input could be an order, with features like:
        - The type of item ordered
        - The quantity
        - The time of day
        - The number of employees working
    - The output would be how long the order is expected to take
    - An important step is being able to convey what you’ve learned and created, so people can use it in the future!
    - Sometimes you learn more about your data by looking at the model
