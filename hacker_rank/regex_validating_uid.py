# ABCXYZ company has up to 100 employees.
# The company decides to create a unique identification number 
# (UID) for each of its employees.
# The company has assigned you the task of validating all the 
# randomly generated UIDs.

# A valid UID must follow the rules below:

# It must contain at least 2 uppercase English alphabet characters.
# It must contain at least 3 digits (0 - 9).
# It should only contain alphanumeric characters (a - z, A - Z & 0 - 9).
# No character should repeat.
# There must be exactly 10 characters in a valid UID.

# Input Format

# The first line contains an integer T, the number of test cases.
# The next T lines contains an employee's UID.

# Output Format

# For each test case, print 'Valid' if the UID is valid. Otherwise, 
# print 'Invalid', on separate lines. Do not print the quotation marks.

# Sample Input

# 2
# B1CD102354
# B1CDEF2354

# Sample Output

# Invalid
# Valid

# Explanation

# B1CD102354: 1 is repeating → Invalid
# B1CDEF2354: Valid

# Enter your code here. Read input from STDIN. Print output to STDOUT

import re

if __name__ == '__main__':

    # create function to check the UID
    def check_UID(uid):

        # check if it has 10 characters
        if len(uid) != 10:
            return False

        # check if it has at least 2 uppercase letters
        if len(re.findall(r'[A-Z]', uid)) < 2:
            return False

        # check if it has at least 3 digits
        if len(re.findall(r'\d', uid)) < 3:
            return False

        # check if it has only alphanumeric characters
        if re.search(r'[^a-zA-Z0-9]', uid):
            return False

        # check if it has no repeating characters
        if re.search(r'(.).*\1', uid):
            return False

        return True

    # get number of test cases
    T = int(input())

    # loop through test cases
    for _ in range(T):

        # get UID
        uid = input()

        # check if UID is valid
        if check_UID(uid):
            print('Valid')
        else:
            print('Invalid')