# You are given a spreadsheet that contains a list of N athletes 
# and their details (such as age, height, weight and so on). 
# You are required to sort the data based on the Kth attribute 
# and print the final resulting table. Follow the example given 
# below for better understanding.

# Rank  Age   Height(in cm)        Rank  Age   Height(in cm)
# 1     32        190               5    24       176
# 2     35        175               4    26       195
# 3     41        188               1    32       190
# 4     26        195               2    35       175
# 5     24        176               3    41       188

# Note that K is indexed from 0 to M - 1, where M is the number of attributes.

# Note: If two attributes are the same for different rows, for example, 
# if two atheletes are of the same age, print the row that appeared first 
# in the input.

# Input Format

# The first line contains N and M separated by a space.
# The next N lines each contain M elements.
# The last line contains K.

# Constraints

# 1 < N, M <= 1000
# 0 <= K < M
# Each element <= 1000

# Output Format

# Print the N lines of the sorted table. Each line should contain the
# space separated elements. Check the sample below for clarity.

# Sample Input 0

# 5 3
# 10 2 5
# 7 1 0
# 9 9 9
# 1 23 12
# 6 5 9
# 1

# Sample Output 0

# 7 1 0
# 10 2 5
# 6 5 9
# 9 9 9
# 1 23 12

# Explanation 0

# The details are sorted based on the second attribute, since K is zero-indexed.

#!/bin/python3

import math
import os
import random
import re
import sys

def sort_func(value):

    # value is a list of integers
    # this returns the item at the k position in the list
    return value[k]

if __name__ == '__main__':
    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    k = int(input())

    # this sorts the list of lists by the kth item in each list
    arr.sort(key=sort_func)

    # loop through the list of lists and print each item in the list
    for i in range(n):

        print(*arr[i])