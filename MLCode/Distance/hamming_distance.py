# Instead of finding the distance between each dimension. Hamming distance only cares about whether the dimensions are exactly equal 
# When finding Hamming distance between two points, add 1 for every dimension that has different values
# Mainly used in spell checking algorithms

def hamming_distance(pt1, pt2):
    distance = 0

    for i in range(len(pt1)):
        # If not equal, add 1 to distance
        if pt1[i] != pt2[i]:
            distance += 1

    return distance

print(hamming_distance([1, 2], [1, 100]))
print(hamming_distance([5, 4, 9], [1, 7, 9]))