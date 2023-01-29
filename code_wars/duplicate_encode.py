# The goal of this exercise is to convert a string to a new string 
# where each character in the new string is "(" if that character 
# appears only once in the original string, or ")" if that character 
# appears more than once in the original string. Ignore capitalization 
# when determining if a character is a duplicate.

# Examples
# "din"      =>  "((("
# "recede"   =>  "()()()"
# "Success"  =>  ")())())"
# "(( @"     =>  "))((" 
# Notes
# Assertion messages may be unclear about what they display in some 
# languages. If you read "...It Should encode XXX", the "XXX" is the 
# expected result, not the input!

def duplicate_encode(word):
    #your code here

    # create a dictionary to store the count of each character
    char_count = {}

    # iterate through the word
    for char in word.lower():

        # if the character is not in the dictionary, add it
        if char not in char_count:
            char_count[char] = 1

        # if the character is in the dictionary, increment its count
        else:
            char_count[char] += 1

    # create a new string to store the encoded word
    encoded_word = ""

    # iterate through the word
    for char in word.lower():
            
            # if the character appears more than once, add a closing parenthesis
            if char_count[char] > 1:
                encoded_word += ")"
    
            # if the character appears only once, add an opening parenthesis
            else:
                encoded_word += "("

    return encoded_word

# import codewars_test as test
# from solution import duplicate_encode

# @test.describe("Duplicate Encoder")
# def fixed_tests():
#     @test.it('Basic Test Cases')
#     def basic_test_cases():
#         test.assert_equals(duplicate_encode("din"),"(((")
#         test.assert_equals(duplicate_encode("recede"),"()()()")
#         test.assert_equals(duplicate_encode("Success"),")())())","should ignore case")
#         test.assert_equals(duplicate_encode("(( @"),"))((")