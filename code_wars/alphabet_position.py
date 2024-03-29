# Welcome.

# In this kata you are required to, given a string, replace every letter 
# with its position in the alphabet.

# If anything in the text isn't a letter, ignore it and don't return it.

# "a" = 1, "b" = 2, etc.

# Example
# alphabet_position("The sunset sets at twelve o' clock.")
# Should return "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11" ( as a string )

def alphabet_position(text):

    # create a variable for all the alphabets
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    # convert the text to lower case
    text = text.lower()

    # create a list to store the result
    result = []

    # loop through the text
    for letter in text:

        # check if the letter is in the alphabet variable
        if letter in alphabet:

            # if it is, append the index of the letter + 1 to the result list
            result.append(str(alphabet.index(letter) + 1))

    # return the result list as a string
    return " ".join(result)

# from random import randint
# test.assert_equals(alphabet_position("The sunset sets at twelve o' clock."), "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11")
# test.assert_equals(alphabet_position("The narwhal bacons at midnight."), "20 8 5 14 1 18 23 8 1 12 2 1 3 15 14 19 1 20 13 9 4 14 9 7 8 20")

# number_test = ""
# for item in range(10):
#     number_test += str(randint(1, 9))
# test.assert_equals(alphabet_position(number_test), "")