# Given an array of integers.

# Return an array, where the first element is the count of positives 
# numbers and the second element is sum of negative numbers. 0 is 
# neither positive nor negative.

# If the input is an empty array or is null, return an empty array.

# Example
# For input [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15], 
# you should return [10, -65].



# import codewars_test as test
# from solution import count_positives_sum_negatives

# @test.describe("Fixed Tests")
# def basic_tests():
#     @test.it('Basic Test Cases')
#     def basic_test_cases():
#         test.assert_equals(count_positives_sum_negatives([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15]),[10,-65])
#         test.assert_equals(count_positives_sum_negatives([0, 2, 3, 0, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14]),[8,-50])
#         test.assert_equals(count_positives_sum_negatives([1]),[1,0])
#         test.assert_equals(count_positives_sum_negatives([-1]),[0,-1])
#         test.assert_equals(count_positives_sum_negatives([0,0,0,0,0,0,0,0,0]),[0,0])
#         test.assert_equals(count_positives_sum_negatives([]),[])