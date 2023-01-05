# You are given a string and your task is to swap cases. In other words, 
# convert all lowercase letters to uppercase letters and vice versa.

# For Example:
# Www.HackerRank.com → wWW.hACKERrANK.COM
# Pythonist 2 → pYTHONIST 2  

# Function Description
# Complete the swap_case function in the editor below.

# swap_case has the following parameters:
# - string s: the string to modify

# Returns
# - string: the modified string

# Input Format
# A single line containing a string s.

# Constraints
# 0 < len(s) <= 1000

# Sample Input 0
# HackerRank.com presents "Pythonist 2".

# Sample Output 0
# hACKERrANK.COM PRESENTS "pYTHONIST 2".

def swap_case(s):

    # create an empty string variable to hold the swapped case
    swapped = ''

    # loop through each letter in the string
    for letter in s:

        # if the letter is in upper case, convert it to lowercase and updated the swapped case variable
        # else, convert it to upper case and return the swapped case
        if (letter.isupper()) == True:
            swapped += (letter.lower())
        else:
            swapped += (letter.upper())
    return swapped

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)