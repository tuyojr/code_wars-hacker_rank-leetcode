# Write a function that takes an array of strings as an argument and 
# returns a sorted array containing the same strings, ordered from 
# shortest to longest.

# For example, if this array were passed as an argument:

# ["Telescopes", "Glasses", "Eyes", "Monocles"]

# Your function would return the following array:

# ["Eyes", "Glasses", "Monocles", "Telescopes"]

# All of the strings in the array passed to your function will be different 
# lengths, so you will not have to decide how to order multiple strings of 
# the same length.



# import codewars_test as test
# from solution import sort_by_length

# @test.describe("Fixed Tests")
# def fixed_tests():
#     @test.it('Basic Test Cases')
#     def basic_test_cases():

#         tests = [
#             [["i", "to", "beg", "life"], ["beg", "life", "i", "to"]],
#             [["", "pizza", "brains", "moderately"], ["", "moderately", "brains", "pizza"]],
#             [["short", "longer", "longest"], ["longer", "longest", "short"]],
#             [["a", "of", "dog", "food"], ["dog", "food", "a", "of"]],
#             [["", "bees", "eloquent", "dictionary"], ["", "dictionary", "eloquent", "bees"]],
#             [["a short sentence", "a longer sentence", "the longest sentence"], ["a longer sentence", "the longest sentence", "a short sentence"]],
#         ]
        
#         for exp, inp in tests:
#             test.assert_equals(sort_by_length(inp), exp)