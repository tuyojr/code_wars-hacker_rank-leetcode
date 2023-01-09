# Given an integer, n, print the following values for each integer i from 1 to n:

# - Decimal
# - Octal
# - Hexadecimal (capitalized)
# - Binary

# Function Description
# Complete the print_formatted function in the editor below.
# print_formatted has the following parameters:
# - int number: the maximum value to print

# Prints
# The four values must be printed on a single line in the order specified above for 
# each i from 1 to number. Each value should be space-padded to match the width of 
# the binary value of number and the values should be separated by a single space.

# Input Format
# A single integer denoting n.

# Constraints
# 1 <= n <= 99

# Sample Input
# 17

# Sample Output

#     1     1     1     1
#     2     2     2    10
#     3     3     3    11
#     4     4     4   100
#     5     5     5   101
#     6     6     6   110
#     7     7     7   111
#     8    10     8  1000
#     9    11     9  1001
#    10    12     A  1010
#    11    13     B  1011
#    12    14     C  1100
#    13    15     D  1101
#    14    16     E  1110
#    15    17     F  1111
#    16    20    10 10000
#    17    21    11 10001

def print_formatted(number):
    # your code goes here

    # create a variable to store the width of the binary value of number
    # [2:] is to start from the number part, ignoring the '0b'
    width = len(bin(number)[2:])

    # loop through the range of the number starting from 1, through the length of the number + 1
    # to account for index 0, since we are starting count from 1
    for i in range(1, number + 1):

        # print the columns in the order...
        # - str(int) value of i when the loop runs, use .rjust(width) to position it the right
        # - str(oct) value of i. [2:] ignores the 0o part
        # - str(hex) value of i. [2:] ignores the 0x part and .upper converts the letters to uppercase
        # - str(bin) value of i. [2:] ignores the 0b part
        print(str(i).rjust(width), str(oct(i)[2:]).rjust(width), str(hex(i)[2:]).upper().rjust(width), str(bin(i)[2:]).rjust(width))

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)