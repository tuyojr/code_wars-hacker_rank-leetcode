# Your goal in this kata is to implement a difference function, 
# which subtracts one list from another and returns the result.

# It should remove all values from list a, which are present in 
# list b keeping their order.

# array_diff([1,2],[1]) == [2]
# If a value is present in b, all of its occurrences must be 
# removed from the other:

# array_diff([1,2,2,2,3],[2]) == [1,3]

def array_diff(a, b):
    #your code here
    for num in b:
        while num in a:
            a.remove(num)
    return a
    # one line solution
    # return [num for num in a if num not in b]

# import codewars_test as test
# from solution import array_diff

# @test.describe("Fixed Tests")
# def fixed_tests():
#     @test.it('Basic Test Cases')
#     def basic_test_cases():
#         test.assert_equals(array_diff([1,2], [1]), [2], "a was [1,2], b was [1], expected [2]")
#         test.assert_equals(array_diff([1,2,2], [1]), [2,2], "a was [1,2,2], b was [1], expected [2,2]")
#         test.assert_equals(array_diff([1,2,2], [2]), [1], "a was [1,2,2], b was [2], expected [1]")
#         test.assert_equals(array_diff([1,2,2], []), [1,2,2], "a was [1,2,2], b was [], expected [1,2,2]")
#         test.assert_equals(array_diff([], [1,2]), [], "a was [], b was [1,2], expected []")
#         test.assert_equals(array_diff([1,2,3], [1, 2]), [3], "a was [1,2,3], b was [1, 2], expected [3]")