# This kata is from check py.checkio.org

# You are given an array with positive numbers and a non-negative number N.
# You should find the N-th power of the element in the array with the index N.
# If N is outside of the array, then return -1. Don't forget that the first
# element has the index 0.

# Let's look at a few examples:

# array = [1, 2, 3, 4] and N = 2, then the result is 3^2 == 9;
# array = [1, 2, 3] and N = 3, but N is outside of the array, so the result is -1.

def index(array, n):
    return array[n] ** n if n < len(array) else -1

# import codewars_test as test
# from solution import index

# @test.describe("Fixed Tests")
# def fixed_tests():
#     @test.it('Basic Test Cases')
#     def basic_test_cases():
#         test.assert_equals(index([1, 2, 3, 4],2),9)
#         test.assert_equals(index([5, 6], 0), 1)
#         test.assert_equals(index([1, 3, 10, 100],3),1000000)
