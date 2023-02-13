# Your task is to make a function that can take any non-negative integer as 
# an argument and return it with its digits in descending order. Essentially, 
# rearrange the digits to create the highest possible number.

# Examples:
# Input: 42145 Output: 54421

# Input: 145263 Output: 654321

# Input: 123456789 Output: 987654321



# import codewars_test as test

# try:
#     from solution import Descending_Order as descending_order
# except ImportError:
#     from solution import descending_order

# @test.describe("Fixed Tests")
# def fixed_tests():
#     @test.it('Basic Test Cases')
#     def basic_test_cases():
#         test.assert_equals(descending_order(0), 0)
#         test.assert_equals(descending_order(15), 51)
#         test.assert_equals(descending_order(123456789), 987654321)