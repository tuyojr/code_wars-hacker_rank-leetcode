# A pangram is a sentence that contains every single letter of the 
# alphabet at least once. For example, the sentence:
# "The quick brown fox jumps over the lazy dog" 
# is a pangram, because it uses the letters A-Z at least once 
# (case is irrelevant).

# Given a string, detect whether or not it is a pangram. Return 
# True if it is, False if not. Ignore numbers and punctuation.

def is_pangram(s):

    # create a string of all the letters in the alphabet
    alphabets = "abcdefghijklmnopqrstuvwxyz"

    # loop through the string of alphabets
    for letter in alphabets:

        # if the letter is not in the string s, return False
        if letter not in s.lower():
            return False
    
    # if the loop completes, return True
    return True

# from solution import is_pangram
# import codewars_test as test

# @test.describe("sample tests")
# def sample_tests():
    
#     @test.it("Should return true for a pangram")
#     def test_pangram():        
#         test.assert_equals(is_pangram("The quick, brown fox jumps over the lazy dog!"), True)

#     @test.it("Should return false for not a pangram")
#     def test_not_pangram():        
#         test.assert_equals(is_pangram("1bcdefghijklmnopqrstuvwxyz"), False)