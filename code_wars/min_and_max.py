# Your task is to make two functions ( max and min, or maximum and minimum, 
# etc., depending on the language ) that receive a list of integers as input, 
# and return the largest and lowest number in that list, respectively.

# Examples (Input -> Output)
# * [4,6,2,1,9,63,-134,566]         -> max = 566, min = -134
# * [-52, 56, 30, 29, -54, 0, -110] -> min = -110, max = 56
# * [42, 54, 65, 87, 0]             -> min = 0, max = 87
# * [5]                             -> min = 5, max = 5
# Notes
# You may consider that there will not be any empty arrays/vectors.

def minimum(arr):
    #your code here...
    return min(arr)

def maximum(arr):
    #...and here
    return max(arr)

# import codewars_test as test
# from solution import minimum, maximum

# try:
#     minimum = minimun
#     maximum = maximun
# except:
#     pass

# @test.describe("Fixed Tests")
# def fixed_tests():
#     @test.it('Fixed min')
#     def fixed_min_cases():
#         test.assert_equals(minimum([-52, 56, 30, 29, -54, 0, -110]), -110)
#         test.assert_equals(minimum([42, 54, 65, 87, 0]), 0)
#         test.assert_equals(minimum([1, 2, 3, 4, 5, 10]), 1)
#         test.assert_equals(minimum([-1, -2, -3, -4, -5, -10]), -10)
#         test.assert_equals(minimum([9]), 9)

#     @test.it('Fixed max')
#     def fixed_min_cases():
#         test.assert_equals(maximum([-52, 56, 30, 29, -54, 0, -110]), 56)
#         test.assert_equals(maximum([4,6,2,1,9,63,-134,566]), 566)
#         test.assert_equals(maximum([5]), 5)
#         test.assert_equals(maximum([534,43,2,1,3,4,5,5,443,443,555,555]), 555)
#         test.assert_equals(maximum([9]), 9)