# You get an array of numbers, return the sum of all of the positives ones.

# Example [1,-4,7,12] => 1 + 7 + 12 = 20

# Note: if there is nothing to sum, the sum is default to 0.

def positive_sum(arr):
    # Your code here
    new_arr = []
    
    for i in arr:
        if i > 0:
            new_arr.append(i)
    return sum(new_arr)
    # one line solution
    # return sum([x for x in arr if x > 0])

# import codewars_test as test
# from solution import positive_sum

# @test.describe("positive_sum")
# def fixed_tests():
#     @test.it('Basic Test Cases')
#     def basic_test_cases():
#         test.assert_equals(positive_sum([1,2,3,4,5]),15)
#         test.assert_equals(positive_sum([1,-2,3,4,5]),13)
#         test.assert_equals(positive_sum([-1,2,3,4,-5]),9)
        
#     @test.it("returns 0 when array is empty")
#     def empty_case():
#         test.assert_equals(positive_sum([]),0)      
        
#     @test.it("returns 0 when all elements are negative")
#     def negative_case():
#         test.assert_equals(positive_sum([-1,-2,-3,-4,-5]),0)