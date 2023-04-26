# Complete the function that takes a non-negative integer n as input, 
# and returns a list of all the powers of 2 with the exponent ranging 
# from 0 to n ( inclusive ).

# Examples
# n = 0  ==> [1]        # [2^0]
# n = 1  ==> [1, 2]     # [2^0, 2^1]
# n = 2  ==> [1, 2, 4]  # [2^0, 2^1, 2^2]

def powers_of_two(n):
    return [2**number for number in range(0, n+1)]

# import codewars_test as test
# from solution import powers_of_two

# @test.describe("Fixed Tests")
# def fixed_tests():
#     @test.it('Basic Test Cases')
#     def basic_test_cases():
#         test.assert_equals(powers_of_two(0), [1])
#         test.assert_equals(powers_of_two(1), [1, 2])
#         test.assert_equals(powers_of_two(4), [1, 2, 4, 8, 16])