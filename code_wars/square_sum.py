# Complete the square sum function so that it squares each number 
# passed into it and then sums the results together.

# For example, for [1, 2, 2] it should return 9 because 1^2 + 2^2 + 2^2 = 9.

def square_sum(numbers):
    # your code here
    squared = list()
    
    for i in numbers:
        squared.append(i*i)
    return sum(squared)
    # return sum([x**2 for x in numbers])

# import codewars_test as test
# from solution import square_sum

# @test.describe("Fixed Tests")
# def basic_tests():
#     @test.it('Basic Test Cases')
#     def basic_test_cases():
#         test.assert_equals(square_sum([1,2]), 5)
#         test.assert_equals(square_sum([0, 3, 4, 5]), 50)
#         test.assert_equals(square_sum([]), 0)
#         test.assert_equals(square_sum([-1,-2]), 5)
#         test.assert_equals(square_sum([-1,0,1]), 2)