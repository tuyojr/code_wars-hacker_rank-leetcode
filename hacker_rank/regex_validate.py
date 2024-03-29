# Let's dive into the interesting topic of regular expressions! 
# You are given some input, and you are required to check whether 
# they are valid mobile numbers.

# A valid mobile number is a ten digit number starting with a 7, 8, or 9.

# Concept

# A valid mobile number is a ten digit number starting with a  or .

# Regular expressions are a key concept in any programming language. 
# A quick explanation with Python examples is available here.
# https://www.thelearningpoint.net/computer-science/learning-python-programming-and-data-structures/learning-python-programming-and-data-structures--tutorial-13--regular-expression-matching

# You could also go through the link below to read more about 
# regular expressions in Python.
# https://developers.google.com/edu/python/regular-expressions

# Input Format

# The first line contains an integer N, the number of inputs.
# N lines follow, each containing some string.

# Constraints

# 1 <= N <= 10
# 2 <= len(Number) <= 15

# Output Format

# For every string listed, print "YES" if it is a valid mobile number 
# and "NO" if it is not on separate lines. Do not print the quotes.

# Sample Input

# 2
# 9587456281
# 1252478965

# Sample Output

# YES
# NO

# Enter your code here. Read input from STDIN. Print output to STDOUT

import re

if __name__ == '__main__':
    N = int(input())
    for i in range(N):
        s = input()
        if re.match(r'^[789]\d{9}$', s):
            print('YES')
        else:
            print('NO')