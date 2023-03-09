# Write a function which calculates the average of the numbers 
# in a given list.

# Note: Empty arrays should return 0.

def find_average(numbers):
    # your code here
    return 0 if len(numbers) == 0 else (sum(numbers) / len(numbers))

# import codewars_test as test
# from solution import find_average

# @test.describe("Fixed Tests")
# def fixed_tests():
#     @test.it('Basic Test Cases')
#     def basic_test_cases():
#         test.assert_equals(find_average([1, 2, 3]), 2)