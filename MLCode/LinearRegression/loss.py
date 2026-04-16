# When we think about how we can set a slope and intercept to a set of points, we need to determine what the best fit is
# For each data point, we calculate "loss"
# "Loss" is a number that measures how bad the models prediction was. Also referred to as "Error"
# "Loss" is calculated by measuring the *squared distance* from the point to the line

def calc_loss(y = [], yPrediction = []):
    totalLoss = 0

    # ensure both are same size
    if len(y) != len(yPrediction):
        raise ValueError("Need an equal length of points")
    
    for i in range(len(y)):
        yv = y[i]
        yp = yPrediction[i]
        totalLoss += (yv - yp) ** 2
    
    return totalLoss

def findMin(values = []):
    min = 0
    for i in range(len(values)):
        if i == 0:
            min = values[i]
        elif values[i] < min:
            min = values[i]
    
    return min
        
# Example data
x = [1, 2, 3]
y = [5, 1, 3]

# first slope and intercept
mOne = 1
bOne = 0

# second slope and intercept
mTwo = 0.5
bTwo = 1

# finding the first set of y values with weights mOne and bOne
yPredictedOne = [mOne * xv + bOne for xv in x]

# finding the second set of y values with weights mOne and bOne
yPredictedTwo = [mTwo * xv + bTwo for xv in x]


# Caluculate the loss with the first set of y predictions
totalLossOne = calc_loss(y, yPredictedOne)

# Caluculate the loss with the second set of y predictions
totalLossTwo = calc_loss(y, yPredictedTwo)

print(totalLossOne)
print(totalLossTwo)

values = [totalLossOne, totalLossTwo]
print("Lowest loss is", str(findMin(values)))