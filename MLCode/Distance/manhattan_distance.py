# Formula is extremely similar to Euclidean distance
# Only difference is we sum the absolute value between each dimension

def manhattan_distance(pt1, pt2):
    distance = 0

    for i in range(len(pt1)): 
        sum = pt1[i] - pt2[i]
        distance += abs(sum)

    return distance