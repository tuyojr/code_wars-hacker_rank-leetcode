# Given the triangle of consecutive odd numbers:

#              1
#           3     5
#        7     9    11
#    13    15    17    19
# 21    23    25    27    29
# ...
# Calculate the sum of the numbers in the nth row of this triangle 
# (starting at index 1) e.g.: (Input --> Output)

# 1 -->  1
# 2 --> 3 + 5 = 8

def row_sum_odd_numbers(n):
    #your code here
    
    # create a variable to hold the total of each row
    total = 0
    
    # calculate the starting number of each row
    start = (n * n) - (n - 1)
    
    # calculate the end of each row
    end = start + n * 2
    
    # loop through each row and increment by two to only count the odd numbers
    for odd_num in range(start, end, 2):
        
        # for each iteration, update the total variable
        total += odd_num
    
    # return the total sum of odd numbers in each row
    return total

# shorter solution
# the cube product is equal to the total sum of odd numbers. MIND BLOWING!
# return n ** 3

# import codewars_test as test
# from solution import row_sum_odd_numbers

# @test.describe("Fixed Tests")
# def fixed_tests():
#     @test.it('Basic Test Cases')
#     def basic_test_cases():
#         test.assert_equals(row_sum_odd_numbers(1), 1)
#         test.assert_equals(row_sum_odd_numbers(2), 8)
#         test.assert_equals(row_sum_odd_numbers(13), 2197)
#         test.assert_equals(row_sum_odd_numbers(19), 6859)
#         test.assert_equals(row_sum_odd_numbers(41), 68921)