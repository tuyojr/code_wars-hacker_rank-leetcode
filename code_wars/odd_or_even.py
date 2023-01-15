# Task:
# Given a list of integers, determine whether the sum of its elements is 
# odd or even.

# Give your answer as a string matching "odd" or "even".

# If the input array is empty consider it as: [0] (array with a zero).

# Examples:
# Input: [0]
# Output: "even"

# Input: [0, 1, 4]
# Output: "odd"

# Input: [0, -1, -5]
# Output: "even"
# Have fun!

def odd_or_even(arr):
    # your code here
    if (sum(arr) %2 != 0):
        return "odd"
    return "even"

# import codewars_test as test
# from solution import odd_or_even

# @test.describe("Fixed Tests")
# def fixed_tests():
#     @test.it('Basic Test Cases')
#     def basic_test_cases():
#         test.assert_equals(odd_or_even([0, 1, 2]), "odd")
#         test.assert_equals(odd_or_even([0, 1, 3]), "even")
#         test.assert_equals(odd_or_even([1023, 1, 2]), "even")