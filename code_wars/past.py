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

def past(h, m, s):
    # Good Luck!
    # hrs * 3600000 ===> milliseconds
    # mins * 60000 ===> milliseconds
    # secs * 1000 ===> milliseconds
    
    # check against the given constraints and return a sum of hour, mins and secs
    # already converted to ms with the conversion keys above
    if 0 <= h <= 23 and 0 <= m <= 59 and 0 <= s <= 59:
        return ((h * 3600000) + (m * 60000) + (s * 1000))

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