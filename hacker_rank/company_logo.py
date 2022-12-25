# A newly opened multinational brand has decided to base their 
# company logo on the three most common characters in the company 
# name. They are now trying out various combinations of company n
# ames and logos based on this condition. Given a string s, which 
# is the company name in lowercase letters, your task is to find 
# the top three most common characters in the string.

# - Print the three most common characters along with their occurrence count.
# - Sort in descending order of occurrence count.
# - If the occurrence count is the same, sort the characters in 
#   alphabetical order.

# For example, according to the conditions described above,

# GOOGLE would have it's logo with the letters G, O, E.

# Input Format
# A single line of input containing the string S.

# Constraints
# 3 < len(S) <= 10^4
# S has at least  distinct characters

# Output Format
# Print the three most common characters along with their occurrence count 
# each on a separate line.
# Sort output in descending order of occurrence count.
# If the occurrence count is the same, sort the characters in alphabetical order.

# Sample Input 0
# aabbbccde

# Sample Output 0
# b 3
# a 2
# c 2

# Explanation 0
# aabbbccde

# Here, b occurs 3 times. It is printed first.
# Both a and c occur 2 times. So, a is printed in the second line and c in the 
# third line because a comes before c in the alphabet.

# Note: The string S has at least 3 distinct characters.

#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    
    # convert the user input to a list
    s = list(input())
    
    # import Counter module to sort the input as keys into a 
    # dict with their number of occurrence as values
    from collections import Counter
    alphabets_counter = Counter(s)
    
    # user the most_common() method to get the most frequent input
    most_common = alphabets_counter.most_common()
    
    # import the OrderedDict module to organize the input in the order
    # the user put them
    from collections import OrderedDict
    arrangements = OrderedDict()
    
    # loop through each most_common values
    for item in most_common:
        
        # check if the length of the dictionary is less than the required
        if len(arrangements.keys()) <= 2:
            
            # update the OrderedDict with the 2nd item, and as the key, and a list as the value
            # the list is updated with the 1st item at each iteration
            arrangements[item[1]] = arrangements.get(item[1], list()) + [item[0]]
            
    # create a count variable to keep track of the required letter
    count = 3
    
    # loop through each key in the new OrderedDict
    for key in arrangements.keys():
        
        # create a variable to hold the letter. this letter is the sorted
        # key of the OrderedDict
        letters = sorted(arrangements[key])
        
        # loop through each letter in the list of letters
        for letter in letters:
            
            # print the letter and the number of times they occur.
            print(letter + " " + str(key))
            
            # decrement the count variable so that we break out of the loop when we reach 0
            count -= 1
            if count == 0:
                break
        if count == 0:
                break