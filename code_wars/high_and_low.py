# In this little assignment you are given a string of space separated 
# numbers, and have to return the highest and lowest number.

# Examples
# high_and_low("1 2 3 4 5")  # return "5 1"
# high_and_low("1 2 -3 4 5") # return "5 -3"
# high_and_low("1 9 3 4 -5") # return "9 -5"
# Notes
# All numbers are valid Int32, no need to validate them.
# There will always be at least one number in the input string.
# Output string must be two numbers separated by a single space, and 
# highest number is first.

def high_and_low(numbers):
    # ...

    # create a list of all the numbers
    nums = list(numbers.split(' '))

    # convert the list to a tuple so we can use the max and min methods
    nums = tuple(eval(i) for i in nums)

    # return the max and min numbers in the tuple
    return f'{max(nums)} {min(nums)}'

# import codewars_test as test
# from solution import high_and_low

# @test.describe("Example Tests")
# def fixed_tests():
#     @test.it('Test Case 1')
#     def basic_test_cases():
#         test.assert_equals(high_and_low("8 3 -5 42 -1 0 0 -9 4 7 4 -4"), "42 -9");
#     @test.it('Test Case 2')
#     def basic_test_cases():
#         test.assert_equals(high_and_low("1 2 3"), "3 1");