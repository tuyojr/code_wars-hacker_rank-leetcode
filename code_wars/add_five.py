# Fix the function
# I created this function to add five to any number that was passed in to it and 
# return the new value. It doesn't throw any errors but it returns the wrong number.

# def add_five(num):
#     total = num + 5
#     return num

# Can you help me fix the function?

def add_five(num):
  total = num + 5
  return total

# import codewars_test as test
# from solution import add_five

# @test.describe('fix add five')
# def fixed_tests():

#     # Basic Tests: Test the basic behavior (basic understanding of the task).
#     @test.it('Basic Test Cases')
#     def basic_tests():
#         test.assert_equals(add_five(5), 10)
#         test.assert_equals(add_five(0), 5)
#         test.assert_equals(add_five(-5), 0)
