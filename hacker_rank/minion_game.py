# Kevin and Stuart want to play the 'The Minion Game'.

# Game Rules

# Both players are given the same string, S.
# Both players have to make substrings using the letters of the string S.
# Stuart has to make words starting with consonants.
# Kevin has to make words starting with vowels.
# The game ends when both players have made all possible substrings.

# Scoring
# A player gets +1 point for each occurrence of the substring in the string S.

# For Example:
# String S = BANANA
# Kevin's vowel beginning word = ANA
# Here, ANA occurs twice in BANANA. Hence, Kevin will get 2 Points.

# For better understanding, see below:

# STUART                  KEVIN
# WORDS    SCORE          WORDS    SCORE
# B          1            A          3
# N          2            AN         2
# BA         1            ANA        2
# NA         2            ANAN       1
# BAN        1            ANANA      1
# NAN        1
# BANA       1
# NANA       1
# BANAN      1
# BANANA     1
# TOTAL      12           TOTAL      9

# Your task is to determine the winner of the game and their score.

# Function Description

# Complete the minion_game in the editor below.

# minion_game has the following parameters:

# string string: the string to analyze
# Prints

# string: the winner's name and score, separated by a space on one line, 
# or Draw if there is no winner

# Input Format
# A single line of input containing the string S.
# Note: The string S will contain only uppercase letters: [A - Z].

# Constraints
# 0 < len(S) <= 10^6

# Sample Input
# BANANA

# Sample Output
# Stuart 12

# Note :
# Vowels are only defined as AEIOU. In this problem, Y is not considered a vowel.

def minion_game(string):
    # your code goes here
    
    # create variables to keep track of kevin and stuart's scores
    kevin = 0
    stuart = 0
    
    # create a variable to hold the length of the string
    length = len(s) 
    
    # loop through each letter in the length of the string
    for letter in range(length):
        
        # if each letter in the input is a vowel, update player's score
        if string[letter] in 'AEIOU':
            
            # kevin's score is the sum of kevin's initial score added
            # to the difference between the length and the index of the letter
            # the same goes for stuart
            kevin = kevin+(length-letter)
        else:
            stuart = stuart+(length-letter)

    # if kevin's score is greater than stuart's score, we print kevin as the winner. Vice versa
    # if they're equal we print a DRAW
    if(kevin>stuart):
        print(f"Kevin {kevin}")
    elif(kevin==stuart):
        print("Draw")
    else:
        print(f"Stuart {stuart}")
            
if __name__ == '__main__':
    s = input()
    minion_game(s)