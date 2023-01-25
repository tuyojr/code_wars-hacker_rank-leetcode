# Given an array of integers as strings and numbers, return 
# the sum of the array values as if all were numbers.

# Return your answer as a number.

def sum_mix(arr):
    # Your code here
    # create a list to hold the numbers
    num_list = []
    
    # loop through the array
    for num in arr:
        # convert the string to an integer and add it to the list
        num_list.append(int(num))
    
    # return the sum of the numbers in the list
    return sum(num_list)

    # # one line solution
    # return sum(map(int, arr))

# import codewars_test as test
# from solution import sum_mix

# @test.describe("Fixed Tests")
# def fixed_tests():
#     @test.it('Basic Test Cases')
#     def basic_test_cases():
#         test.assert_equals(sum_mix([9, 3, '7', '3']), 22)
#         test.assert_equals(sum_mix(['5', '0', 9, 3, 2, 1, '9', 6, 7]), 42)
#         test.assert_equals(sum_mix(['3', 6, 6, 0, '5', 8, 5, '6', 2,'0']), 41)
#         test.assert_equals(sum_mix(['1', '5', '8', 8, 9, 9, 2, '3']), 45)
#         test.assert_equals(sum_mix([8, 0, 0, 8, 5, 7, 2, 3, 7, 8, 6, 7]), 61)