# Transpose
# We can generate the transposition of an array using the tool numpy.transpose.
# It will not affect the original array, but it will create a new array.

# import numpy

# my_array = numpy.array([[1,2,3],
#                         [4,5,6]])
# print numpy.transpose(my_array)

# #Output
# [[1 4]
#  [2 5]
#  [3 6]]

# Flatten
# The tool flatten creates a copy of the input array flattened to one dimension.

# import numpy

# my_array = numpy.array([[1,2,3],
#                         [4,5,6]])
# print my_array.flatten()

# #Output
# [1 2 3 4 5 6]

# Task
# You are given a NxM integer array matrix with space separated elements (N = rows and M = columns).
# Your task is to print the transpose and flatten results.

# Input Format
# The first line contains the space separated values of N and M.
# The next N lines contains the space separated elements of M columns.

# Output Format
# First, print the transpose array and then print the flatten.

# Sample Input
# 2 2
# 1 2
# 3 4

# Sample Output
# [[1 3]
#  [2 4]]
# [1 2 3 4]

import numpy

# create a variable to hold the final array
final_array =[]

# create variables to accept user input for number of rows and columns
N, M = map(int, input().split())

# loop through each row
for values in range(N):

    # update the final array with the numpy array module
    final_array.append(numpy.array(input().split(), int))

# convert the final array from a list to an array
final_array = numpy.asarray(final_array)

# print the transposed and flattened arrays
print(numpy.transpose(final_array), final_array.flatten(), sep="\n")