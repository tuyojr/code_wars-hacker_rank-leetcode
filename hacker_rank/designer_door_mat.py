# Mr. Vincent works in a door mat manufacturing company. One day, 
# he designed a new door mat with the following specifications:
# - Mat size must be N x M. (N is an odd natural number, and  is M times N.)
# - The design should have 'WELCOME' written in the center.
# - The design pattern should only use |, . and - characters.

# Sample Designs

#     Size: 7 x 21 
#     ---------.|.---------
#     ------.|..|..|.------
#     ---.|..|..|..|..|.---
#     -------WELCOME-------
#     ---.|..|..|..|..|.---
#     ------.|..|..|.------
#     ---------.|.---------
    
#     Size: 11 x 33
#     ---------------.|.---------------
#     ------------.|..|..|.------------
#     ---------.|..|..|..|..|.---------
#     ------.|..|..|..|..|..|..|.------
#     ---.|..|..|..|..|..|..|..|..|.---
#     -------------WELCOME-------------
#     ---.|..|..|..|..|..|..|..|..|.---
#     ------.|..|..|..|..|..|..|.------
#     ---------.|..|..|..|..|.---------
#     ------------.|..|..|.------------
#     ---------------.|.---------------

# Input Format
# A single line containing the space separated values of N and M.

# Constraints
# - 5 < N < 101
# - 15 < M < 303

# Output Format
# Output the design pattern.

# Sample Input
# 9 27

# Sample Output

# ------------.|.------------
# ---------.|..|..|.---------
# ------.|..|..|..|..|.------
# ---.|..|..|..|..|..|..|.---
# ----------WELCOME----------
# ---.|..|..|..|..|..|..|.---
# ------.|..|..|..|..|.------
# ---------.|..|..|.---------
# ------------.|.------------

if __name__ == '__main__':

    # prompt the user for input of the mat specification
    N, M = map(int, input().split())

    # Top half

    # loop through the range of the mat specification starting from 1, through
    # the length N of the mat, and an increment(step) of 2 (account for the odd natural numbers)
    for i in range(1, N, 2): 

        # print the mat design using the center method to center the design
        # ".|." * i prints each time the loop runs
        # M is the width and '-' is the character to fill the width
        print((".|." * i).center(M, "-"))
    
    # Middle

    # print the welcome message using the center method to center the message
    print("WELCOME".center(M, "-"))

    # Bottom half

    # loop through the range of the mat specification starting from the length in decreasing order
    for i in range(N-2, -1, -2): 
        print((".|." * i).center(M, "-"))