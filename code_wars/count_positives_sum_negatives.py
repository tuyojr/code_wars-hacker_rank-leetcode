# Given an array of integers.

# Return an array, where the first element is the count of positives 
# numbers and the second element is sum of negative numbers. 0 is 
# neither positive nor negative.

# If the input is an empty array or is null, return an empty array.

# Example
# For input [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15], 
# you should return [10, -65].

def count_positives_sum_negatives(arr):
    
    # if the array is empty or null, return an empty array
    if not arr: return []

    # variable for the initial position where the length of positive numbers will be
    positives_count = 0
    
    # variable for the sum of all negative numbers in the array
    negative_sum = 0
    
    # loop through each item in the array
    for x in arr:
        
        # if the number is positive, increase it's count variable
        if x > 0:
            positives_count += 1
            
        # if the number is negative, add the number to it's sum variable
        elif x < 0:
            negative_sum += x
    
    # return the desired array
    return [positives_count, negative_sum]

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