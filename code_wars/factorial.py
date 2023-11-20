# In mathematics, the factorial of a non-negative integer n, denoted by n!, 
# is the product of all positive integers less than or equal to n. 
# For example: 5! = 5 * 4 * 3 * 2 * 1 = 120. By convention the value of 0! is 1.

# Write a function to calculate factorial for a given input. If input is 
# below 0 or above 12 throw an exception of type ArgumentOutOfRangeException (C#) 
# or IllegalArgumentException (Java) or RangeException (PHP) or throw a 
# RangeError (JavaScript) or ValueError (Python) or return -1 (C).

# More details about factorial can be found here (https://www.wikiwand.com/en/Factorial).

def factorial(n):
        if n < 0 or n > 12:
            raise ValueError("Input must be between 0-12.")
        elif n == 0:
            return 1
        else:
            return n * factorial(n - 1)

# import codewars_test as test
# from solution import factorial

# @test.describe("Fixed Tests")
# def fixed_tests():
#     @test.it('Basic Test Cases')
#     def basic_test_cases():
#         test.assert_equals(factorial(0), 1, "factorial for 0 is 1"),
#         test.assert_equals(factorial(1), 1, "factorial for 1 is 1"),
#         test.assert_equals(factorial(2), 2, "factorial for 2 is 2"),
#         test.assert_equals(factorial(3), 6, "factorial for 3 is 6"), 