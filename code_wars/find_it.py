# Given an array of integers, find the one that appears an odd number of times.

# There will always be only one integer that appears an odd number of times.

# Examples
# [7] should return 7, because it occurs 1 time (which is odd).
# [0] should return 0, because it occurs 1 time (which is odd).
# [1,1,2] should return 2, because it occurs 1 time (which is odd).
# [0,1,0,1,0] should return 0, because it occurs 3 times (which is odd).
# [1,2,2,3,3,3,4,3,3,3,2,2,1] should return 4, because it appears 1 time (which is odd).

def find_it(seq):
    
    # create a dictionary to keep track of all the integers and how many 
    # times they appear
    integers = {}
    
    # loop through each integer in the list and add it to the integers dictionary
    for num in seq:
        integers[num] = integers.get(num, 0) + 1
        
    # loop through the key and values in the dictionary and check if any key has
    # an odd number value, then return that key
    for key, value in integers.items():
        if (value % 2) != 0:
            return key

    # one line solution
    # return [x for x in seq if seq.count(x) % 2][0]

# import codewars_test as test
# from solution import find_it

# @test.describe("Sample tests")
# def sample_tests():
    
#     @test.it("find_it([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]) should return 5 (because it appears 3 times)")
#     def _():
#         test.assert_equals(find_it([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]), 5)
        
#     @test.it("find_it([1,1,2,-2,5,2,4,4,-1,-2,5]) should return -1 (because it appears 1 time)")
#     def _():
#         test.assert_equals(find_it([1,1,2,-2,5,2,4,4,-1,-2,5]), -1);
        
#     @test.it("find_it([20,1,1,2,2,3,3,5,5,4,20,4,5]) should return 5 (because it appears 3 times)")
#     def _():
#         test.assert_equals(find_it([20,1,1,2,2,3,3,5,5,4,20,4,5]), 5);
        
#     @test.it("find_it([10]) should return 10 (because it appears 1 time)")
#     def _():
#         test.assert_equals(find_it([10]), 10);

#     @test.it("find_it([10, 10, 10]) should return 10 (because it appears 3 times)")
#     def _():
#         test.assert_equals(find_it([10, 10, 10]), 10);        
        
#     @test.it("find_it([1,1,1,1,1,1,10,1,1,1,1]) should return 10 (because it appears 1 time)")
#     def _():
#         test.assert_equals(find_it([1,1,1,1,1,1,10,1,1,1,1]), 10);

#     @test.it("find_it([5,4,3,2,1,5,4,3,2,10,10]) should return 1 (because it appears 1 time)")
#     def _():
#         test.assert_equals(find_it([5,4,3,2,1,5,4,3,2,10,10]), 1);