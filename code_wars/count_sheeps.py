# Consider an array/list of sheep where some sheep may be missing from 
# their place. We need a function that counts the number of sheep 
# present in the array (true means present).

# For example,

# [True,  True,  True,  False,
#   True,  True,  True,  True ,
#   True,  False, True,  False,
#   True,  False, False, True ,
#   True,  True,  True,  True ,
#   False, False, True,  True]
# The correct answer would be 17.

# Hint: Don't forget to check for bad values like null/undefined

def count_sheeps(sheep):
    # TODO May the force be with you
    return sheep.count(True)

# import codewars_test as test
# from solution import count_sheeps

# @test.describe("Basic Tests")
# def basic_tests():
    
#     @test.it("Basic Tests")
#     def basic_tests():
#         array1 = [True,  True,  True,  False,
#                   True,  True,  True,  True ,
#                   True,  False, True,  False,
#                   True,  False, False, True ,
#                   True,  True,  True,  True ,
#                   False, False, True,  True ];
        
#         result = count_sheeps(array1)
#         test.assert_equals(result, 17, f"There are 17 sheeps in total, not {result}")