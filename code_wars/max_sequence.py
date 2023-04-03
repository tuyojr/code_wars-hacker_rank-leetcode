# The maximum sum subarray problem consists in finding the maximum sum 
# of a contiguous subsequence in an array or list of integers:

# max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4])
# # should be 6: [4, -1, 2, 1]

# Easy case is when the list is made up of only positive numbers and the 
# maximum sum is the sum of the whole array. If the list is made up of 
# only negative numbers, return 0 instead.

# Empty list is considered to have zero greatest sum. Note that the empty 
# list or array is also a valid sublist/subarray.

def max_sequence(arr):
    #your code here
    # create a variable to hold the max sum
    max_sum = 0
    # create a variable to hold the current sum
    current_sum = 0
    # loop through the array
    for num in arr:
        # add the current number to the current sum
        current_sum += num
        # if the current sum is greater than the max sum
        if current_sum > max_sum:
            # set the max sum to the current sum
            max_sum = current_sum
        # if the current sum is less than 0
        if current_sum < 0:
            # set the current sum to 0
            current_sum = 0
    # return the max sum
    return max_sum

# try:
#     # backwards compatibility
#     from solution import maxSequence as max_sequence
# except ImportError:
#     from solution import max_sequence

# import codewars_test as test

# @test.describe("Fixed tests")
# def tests():
    
#     @test.it("Should work on an empty array")
#     def test_empty_array():
#         test.assert_equals(max_sequence([]), 0)

#     @test.it("Should obtain correct maximum subarray sum in the array from the kata description example")
#     def test_example_array():
#         test.assert_equals(max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4]), 6)
        
#     @test.it("Should obtain correct maximum subarray sum in an example with negative numbers")
#     def test_negative_array():
#         test.assert_equals(max_sequence([-2, -1, -3, -4, -1, -2, -1, -5, -4]), 0)
        
#     @test.it("Should obtain correct maximum subarray sum in a complex example")
#     def test_complex_array():
#         test.assert_equals(max_sequence([7, 4, 11, -11, 39, 36, 10, -6, 37, -10, -32, 44, -26, -34, 43, 43]), 155)