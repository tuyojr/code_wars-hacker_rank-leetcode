# dot
# https://numpy.org/doc/stable/reference/generated/numpy.dot.html
# The dot tool returns the dot product of two arrays.

# import numpy

# A = numpy.array([ 1, 2 ])
# B = numpy.array([ 3, 4 ])

# print numpy.dot(A, B)       #Output : 11

# cross
# https://numpy.org/doc/stable/reference/generated/numpy.cross.html
# The cross tool returns the cross product of two arrays.

# import numpy

# A = numpy.array([ 1, 2 ])
# B = numpy.array([ 3, 4 ])

# print numpy.cross(A, B)     #Output : -2

# Task

# You are given two arrays A and B. Both have dimensions of NxM.
# Your task is to compute their matrix product.
# https://en.wikipedia.org/wiki/Matrix_multiplication#Matrix_product_.28two_matrices.29

# Input Format

# The first line contains the integer N.
# The next N lines contains N space separated integers of array A.
# The following N lines contains N space separated integers of array B.

# Output Format

# Print the matrix multiplication of A and B.

# Sample Input

# 2
# 1 2
# 3 4
# 1 2
# 3 4

# Sample Output

# [[ 7 10]
#  [15 22]]

import numpy

N = int(input())

A = numpy.array([input().split() for _ in range(N)], int)
B = numpy.array([input().split() for _ in range(N)], int)

print(numpy.dot(A, B))