# Count the number of Duplicates
# Write a function that will return the count of distinct case-insensitive 
# alphabetic characters and numeric digits that occur more than once in the 
# input string. The input string can be assumed to contain only alphabets 
# (both uppercase and lowercase) and numeric digits.

# Example
# "abcde" -> 0 ## no characters repeats more than once
# "aabbcde" -> 2 ## 'a' and 'b'
# "aabBcde" -> 2 ## 'a' occurs twice and 'b' twice (`b` and `B`)
# "indivisibility" -> 1 ## 'i' occurs six times
# "Indivisibilities" -> 2 ## 'i' occurs seven times and 's' occurs twice
# "aA11" -> 2 ## 'a' and '1'
# "ABBA" -> 2 ## 'A' and 'B' each occur twice

def duplicate_count(text):
    # Your code goes here
    
    # convert the whole string to lower case
    text = text.lower()

    # create a dictionary for all the characters in the string
    letters = {}

    # loop through the text and update the letters dictionary with each 
    # letter and their number of occurrences
    for letter in text:
        letters[letter] = text.count(letter)
    
    # loop through the dictionary and return the length of keys whose value are
    # greater than or equal to 2
    return len([key for key, value in letters.items() if value >= 2])

# import codewars_test as test
# from solution import duplicate_count

# @test.describe("Fixed Tests")
# def fixed_tests():
#     @test.it("Basic Tests")
#     def basic_tests():
#         test.assert_equals(duplicate_count(""), 0)
#         test.assert_equals(duplicate_count("abcde"), 0)
#         test.assert_equals(duplicate_count("abcdeaa"), 1)
#         test.assert_equals(duplicate_count("abcdeaB"), 2)
#         test.assert_equals(duplicate_count("Indivisibilities"), 2)