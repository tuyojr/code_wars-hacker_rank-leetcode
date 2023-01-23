# You are given a positive integer N.
# Your task is to print a palindromic triangle of size N.

# For example, a palindromic triangle of size 5 is:

# 1
# 121
# 12321
# 1234321
# 123454321

# You can't take more than two lines. The first line (a for-statement) is already written for you.
# You have to complete the code using exactly one print statement.

# Note:
# Using anything related to strings will give a score of 0.
# Using more than one for-statement will give a score of 0.

# Input Format

# A single line of input containing the integer N.

# Constraints
# 0 < N < 10

# Output Format

# Print the palindromic triangle of size N as explained above.

# Sample Input

# 5

# Sample Output

# 1
# 121
# 12321
# 1234321
# 123454321

    # i starts from 1, the first iterations outputs 1 ---> 10**1-1 == 9, 9//9 == 1, 1**2 == 1
    # the second iteration outputs 121 ---> 10**2-1 == 99, 99//9 == 11, 11**2 == 121
    # the third iteration outputs 12321 ---> 10**3-1 == 999, 999//9 == 111, 111**2 == 12321
    # the fourth iteration outputs 1234321 ---> 10**4-1 == 9999, 9999//9 == 1111, 1111**2 == 1234321
    # the fifth iteration outputs 123454321 ---> 10**5-1 == 99999, 99999//9 == 11111, 11111**2 == 123454321
for i in range(1,int(input())+1): #More than 2 lines will result in 0 score. Do not leave a blank line also
    print(((10**i-1)//9)**2)