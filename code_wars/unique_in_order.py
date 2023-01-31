# Implement the function unique_in_order which takes as argument a 
# sequence and returns a list of items without any elements with 
# the same value next to each other and preserving the original 
# order of elements.

# For example:

# unique_in_order('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B']
# unique_in_order('ABBCcAD')         == ['A', 'B', 'C', 'c', 'A', 'D']
# unique_in_order([1, 2, 2, 3, 3])   == [1, 2, 3]
# unique_in_order((1, 2, 2, 3, 3))   == [1, 2, 3]

def unique_in_order(sequence):
    
    # create a list to store the ordered elements
    result = []
    
    # a variable to store the previous character
    prev = None
    
    # loop through the input string
    for char in sequence:
        
        # if the character is not equal to the previous character, add it to the final list
        # and set it as the new value of the previous character
        if char != prev:
            result.append(char)
            prev = char
    
    # return the new unique list
    return result
# import codewars_test as test
# from solution import unique_in_order


# @test.describe("Sample Tests")
# def sample_tests():
#     @test.it("Should work with empty sequence")
#     def _():
#         test.assert_equals(unique_in_order(""), [])
#         test.assert_equals(unique_in_order([]), [])
#         test.assert_equals(unique_in_order(()), [])

#     @test.it("Should work with single element sequence")
#     def _():
#         test.assert_equals(unique_in_order("A"), ["A"])
#         test.assert_equals(unique_in_order(["A"]), ["A"])
#         test.assert_equals(unique_in_order(("A",)), ["A"])

#     @test.it("Should reduce duplicates")
#     def _():
#         test.assert_equals(unique_in_order("AA"), ["A"])
#         test.assert_equals(unique_in_order("AAAABBBCCDAABBB"), ["A", "B", "C", "D", "A", "B"])

#     @test.it("Should be case-sensitive")
#     def _():
#         test.assert_equals(unique_in_order("ABBCcA"), ["A", "B", "C", "c", "A"])

#     @test.it("Should work with different element types")
#     def _():
#         test.assert_equals(unique_in_order([1, 2, 3, 3, -1]), [1, 2, 3, -1])
#         test.assert_equals(unique_in_order(["a", "b", "b", "a"]), ["a", "b", "a"])