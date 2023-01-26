# Write a function to split a string and convert it into an array of words.

# Examples (Input ==> Output):
# "Robin Singh" ==> ["Robin", "Singh"]

# "I love arrays they are my favorite" ==> ["I", "love", "arrays", "they", "are", "my", "favorite"]

def string_to_array(s):
    # your code here
    # split the string into an array of words
    arr = s.split(' ')
    return arr

# import codewars_test as test
# from solution import string_to_array

# @test.describe("Fixed Tests")
# def fixed_tests():
#     @test.it('Basic Test Cases')
#     def basic_test_cases():
#         test.assert_equals(string_to_array("Robin Singh"), ["Robin", "Singh"])
#         test.assert_equals(string_to_array("CodeWars"), ["CodeWars"])
#         test.assert_equals(string_to_array("I love arrays they are my favorite"), ["I", "love", "arrays", "they", "are", "my", "favorite"])
#         test.assert_equals(string_to_array("1 2 3"), ["1", "2", "3"])
#         test.assert_equals(string_to_array(""), [""])