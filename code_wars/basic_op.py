# Your task is to create a function that does four basic mathematical 
# operations.

# The function should take three arguments - operation(string/char), 
# value1(number), value2(number).
# The function should return result of numbers after applying the chosen 
# operation.

# Examples(Operator, value1, value2) --> output
# ('+', 4, 7) --> 11
# ('-', 15, 18) --> -3
# ('*', 5, 5) --> 25
# ('/', 49, 7) --> 7

def basic_op(operator, value1, value2):
    #your code here
    if operator == '+':
        return value1 + value2
    elif operator == '-':
        return value1 - value2
    elif operator == '*':
        return value1 * value2
    elif operator == '/':
        return value1 / value2
    else:
        return "Accepted operators are +, -, *, and /. Run the program again."

    # return eval(f"{value1}{operator}{value2}")

# import codewars_test as test
# from solution import basic_op

# @test.describe("Fixed Tests")
# def fixed_tests():
#     @test.it('Basic Test Cases')
#     def basic_test_cases():
#         test.assert_equals(basic_op('+', 4, 7), 11)
#         test.assert_equals(basic_op('-', 15, 18), -3)
#         test.assert_equals(basic_op('*', 5, 5), 25)
#         test.assert_equals(basic_op('/', 49, 7), 7)