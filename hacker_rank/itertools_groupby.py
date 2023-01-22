# In this task, we would like for you to appreciate the usefulness 
# of the groupby() function of itertools . To read more about this 
# function, Check this out.
# https://docs.python.org/3/library/itertools.html#itertools.groupby

# You are given a string S. Suppose a character 'c' occurs consecutively X 
# times in the string. Replace these consecutive occurrences of the 
# character 'c' with (X, c) in the string.

# For a better understanding of the problem, check the explanation.

# Input Format

# A single line of input consisting of the string S.

# Output Format

# A single line of output consisting of the modified string.

# Constraints

# All the characters of S denote integers between 0 and 9.
# 1 <= |S| <= 10^4

# Sample Input

# 1222311

# Sample Output

# (1, 1) (3, 2) (1, 3) (2, 1)
# Explanation

# First, the character 1 occurs only once. It is replaced by (1, 1). 
# Then the character 2 occurs three times, and it is replaced by (3, 2) 
# and so on.

# Also, note the single space within each compression and between 
# the compressions.

# Enter your code here. Read input from STDIN. Print output to STDOUT

from itertools import groupby

if __name__ == '__main__':

    # prompt the user for input
    S = input()

    # groupby() returns a tuple of the key and the group
    # the key is the first element of the tuple
    # the group is the second element of the tuple
    # the group is a list of the elements in the group
    # the groupby() function groups the elements in the list
    # by the key
    for k, g in groupby(S):

        # print the length of the group and the key
        # the end=' ' argument prints the output on the same line
        print('({}, {})'.format(len(list(g)), k), end=' ')