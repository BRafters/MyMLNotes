We need to know how “far off” a models predictions are from the actual values. The mathematical concept of distance comes into play, offering a quantitative measure of a model’s accuracy
### Different Kinds of Distance

- Measuring distance may feel straightforward, but in practice, there are actually many different kinds of distance
- For example: measuring the distance it takes to travel between two places in a city
    - In a helicopter, the shortest distance might just be the length of a straight line from point A to point B
    - If we are walking, now the shortest distance has to take the structure of the city, blocks, and buildings into account
- Distance depends on context
    - In ML we might measure the “distance” between our prediction and what actually happens in different ways

- **Euclidean Distance:** the most common distance formula. The length of a straight line between two points
- **Manhattan Distance:** the “city block” distance, useful in urban planning models
- **Hamming Distance:** used to measure distance between words in natural language processing
### Euclidean Distance:

- The most commonly used formula
- To find the euclidian distance between two points:
    - We calculate the squared distance between each dimension
    - We add up all the squared distances and take the square root
- The formula looks like. Note “a” is one point and “b” is another point
![[Pasted image 20260415214008.png]]
- This image shows the visual of Euclidean distance being calculated
- ![[euclidean.svg]]
￼
### Manhattan Distance

Called **Manhattan Distance** as it is similar looking to how you might navigate when walking city blocks

- Extremely similar to Euclidean distance
- Rather than summing the squared difference between each dimension, we sum the **absolute value** between each dimension
- If you ever wondered “How many blocks will it take me to get from point A to point B”, you’ve calculated **Manhattan distance**
![[Pasted image 20260415214159.png]]
- Note Manhattan distance will always be greater than or equal to euclidean distance
- A visual of Manhattan distance: ![[manhattan.svg]]
### Hamming Distance

- Instead of finding the distance of each dimension, **Hamming Distance** only cares about whether the dimensions are exactly equal
- When finding the Hamming distance between two points. Add one for every dimension that has different values
- **Hamming Distance** is used in spell checking algorithms
    - The distance between the word “there” and typo “there” is one
        - Each letter is a dimension, and each dimension has the same value except for one
### SciPy

- Pythons SciPy library actually contains these three distance formulas for you
    - SciPy’s implementation of Manhattan distance is called ‘cityblock()’
    - SciPy’s implementation of Hamming distance will always return a number between 0 and 1
        - Rather than summing the number of differences in dimensions
            - This implementation sums those differences, then divides by the total number of dimensions
