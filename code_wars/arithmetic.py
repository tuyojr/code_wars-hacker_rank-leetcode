# Given two numbers and an arithmetic operator (the name of it, as a string), 
# return the result of the two numbers having that operator used on them.

# a and b will both be positive integers, and a will always be the first number 
# in the operation, and b always the second.

# The four operators are "add", "subtract", "divide", "multiply".

# A few examples:(Input1, Input2, Input3 --> Output)

# 5, 2, "add"      --> 7
# 5, 2, "subtract" --> 3
# 5, 2, "multiply" --> 10
# 5, 2, "divide"   --> 2.5

# Try to do it without using if statements!

def arithmetic(a, b, operator):
    #your code here

    # create a dictionary of operators
    operators = {
        'add': a + b,
        'subtract': a - b,
        'multiply': a * b,
        'divide': a / b
    }

    # return the value of the operator
    return operators[operator]

# import codewars_test as test
# from solution import arithmetic

# @test.describe("Fixed Tests")
# def fixed_tests():
#     @test.it('Basic Test Cases')
#     def basic_test_cases():
#         test.assert_equals(arithmetic(1, 2, "add"), 3, "'add' should return the two numbers added together!")
#         test.assert_equals(arithmetic(8, 2, "subtract"), 6, "'subtract' should return a minus b!")
#         test.assert_equals(arithmetic(5, 2, "multiply"), 10, "'multiply' should return a multiplied by b!")
#         test.assert_equals(arithmetic(8, 2, "divide"), 4, "'divide' should return a divided by b!")