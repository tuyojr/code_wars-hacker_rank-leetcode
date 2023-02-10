# start() & end()
# https://docs.python.org/3/library/re.html#re.Match.start
# These expressions return the indices of the start and end of the substring matched by the group.

# Code

# >>> import re
# >>> m = re.search(r'\d+','1234')
# >>> m.end()
# 4
# >>> m.start()
# 0

# Task

# You are given a string S.
# Your task is to find the indices of the start and end of string k in S.

# Input Format

# The first line contains the string S.
# The second line contains the string k.

# Constraints

# 0 < len(S) < 100
# 0 < len(k) < 100

# Output Format

# Print the tuple in this format: (start _index, end _index).
# If no match is found, print (-1, -1).

# Sample Input

# aaadaa
# aa

# Sample Output

# (0, 1)
# (1, 2)
# (4, 5)

# Enter your code here. Read input from STDIN. Print output to STDOUT

import re

if __name__ == '__main__':

    # Create a variable to hold the input string
    S = input()

    # Create a variable to hold the substring to search for
    k = input()

    # Create a variable to hold the pattern to search for
    pattern = re.compile(k)

    # Create a variable to hold the result of the search
    result = pattern.search(S)

    # if the pattern does not match the result, print (-1, -1)
    if not result:
        print('(-1, -1)')

    # if the pattern does match the result, print the start and end indices
    while result:

        # print the start and end indices
        print('({0}, {1})'.format(result.start(), result.end() - 1))

        # search for the next match
        result = pattern.search(S, result.start() + 1)