import math

def euclidean_distance(pt1, pt2):
    distance = 0

    # Take the first dimension of each point, subtract them from each other, then square the value
    # Add it to the distance
    for i in range(len(pt1)):
        a = pt1[i]
        b = pt2[i]
        distance += (a - b) ** 2

    # Square root the current distance value
    return math.sqrt(distance)

print(euclidean_distance([1, 2], [4, 0]))
print(euclidean_distance([5, 4, 3], [1, 7, 9]))