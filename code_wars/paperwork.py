# Your classmates asked you to copy some paperwork for them. 
# You know that there are 'n' classmates and the paperwork has 'm' pages.

# Your task is to calculate how many blank pages do you need. 
# If n < 0 or m < 0 return 0.

# Example:
# n= 5, m=5: 25
# n=-5, m=5:  0
# Waiting for translations and Feedback! Thanks!



# import codewars_test as test
# from solution import paperwork

# @test.describe("Fixed Tests")
# def basic_tests():
#     @test.it('Basic Test Cases')
#     def basic_test_cases():
#         test.assert_equals(paperwork(5,5), 25, "Failed at Paperwork(5,5)")
#         test.assert_equals(paperwork(-5,5), 0, "Failed at Paperwork(-5,5)")
#         test.assert_equals(paperwork(5,-5), 0, "Failed at Paperwork(5,-5)")
#         test.assert_equals(paperwork(-5,-5), 0, "Failed at Paperwork(-5,-5)")
#         test.assert_equals(paperwork(5,0), 0, "Failed at Paperwork(5,0)")