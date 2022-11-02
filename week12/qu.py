"""
Numpy Array Quiz
Question 1
What is the result of the following code?

    import numpy as np
    a = np.array([1, 2, 3])
    b = np.array([4, 5, 6])
    c = a + b
    print(c)
Question 2
Create a numpy array of 10 zeros. and reshape it to (2, 5)

Question 3
Find Mean, Mode, Median, Standard Deviation of the following data

    data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
Question 4
create a 6x6 numpy array with random values and find the min and max values

Question 5
create a 3D numpy array and reshape it to 2D

Question 6
create 1D array from this data

    data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

"""
# solution 

# 1. [5 ,7 ,9]

# Create a numpy array of 10 zeros. and reshape it to (2, 5)

import numpy as np

array = np.zeros(10 , dtype = int).reshape(2, 5)
print(array)

# solution 3
import statistics
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

mean = np.mean(data)

mode = statistics.mode(data)

median = np.median(data)

standard_deviation = np.std(data)

print(f"Mean: {mean}, Mode: {mode}, Median: {median}, Standard Deviation: {standard_deviation}")

#  solution 4 

array = np.random.random((6, 6))

max = np.max(array)

min = np.min(array)

print(f"Max: {max}, Min: {min}")

# solution 5

_3array = np.random.random((3, 3))
print(_3array)

# solution 6
"""
create 1D array from this data

    data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
"""
data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
new_arr = np.array(data)
converted_arr = new_arr.flatten()
print(converted_arr)