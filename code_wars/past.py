# Clock shows h hours, m minutes and s seconds after midnight.

# Your task is to write a function which returns the time since 
# midnight in milliseconds.

# Example:
# h = 0
# m = 1
# s = 1

# result = 61000
# Input constraints:

# 0 <= h <= 23
# 0 <= m <= 59
# 0 <= s <= 59



# import codewars_test as test
# from solution import past

# @test.describe("Fixed Tests")
# def basic_tests():
#     @test.it('Basic Test Cases')
#     def basic_test_cases():
#         test.assert_equals(past(0,1,1),61000)
#         test.assert_equals(past(1,1,1),3661000)
#         test.assert_equals(past(0,0,0),0)
#         test.assert_equals(past(1,0,1),3601000)
#         test.assert_equals(past(1,0,0),3600000)