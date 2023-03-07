# Given two integers a and b, which can be positive or negative, find the sum of all 
# the integers between and including them and return it. If the two numbers are equal return a or b.

# Note: a and b are not ordered!

# Examples (a, b) --> output (explanation)
# (1, 0) --> 1 (1 + 0 = 1)
# (1, 2) --> 3 (1 + 2 = 3)
# (0, 1) --> 1 (0 + 1 = 1)
# (1, 1) --> 1 (1 since both are same)
# (-1, 0) --> -1 (-1 + 0 = -1)
# (-1, 2) --> 2 (-1 + 0 + 1 + 2 = 2)
# Your function should only return a number, not the explanation about how you get that number.

def get_sum(a, b):
  # Your code here
  
  if a < b:
    return sum(list(range(a, b + 1))
  else:
    return sum(list(range(b, a + 1)))

# from solution import get_sum
# import codewars_test as test


# @test.describe('Sum of numbers')
# def desc1():
#     @test.it('Sample tests')
#     def it1():
#         test.assert_equals(get_sum(0,1),1)
#         test.assert_equals(get_sum(0,-1),-1)
