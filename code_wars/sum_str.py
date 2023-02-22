# Create a function that takes 2 integers in form of a string as 
# an input, and outputs the sum (also as a string):

# Example: (Input1, Input2 -->Output)

# "4",  "5" --> "9"
# "34", "5" --> "39"
# "", "" --> "0"
# "2", "" --> "2"
# "-5", "3" --> "-2"

def sum_str(a, b):
    # happy coding !
    if a == "":
        a = 0
    if b == "":
        b = 0
    return str(int(a) + int(b))

# import codewars_test as test
# from solution import sum_str

# @test.describe("Fixed Tests")
# def basic_tests():
    
#     @test.it("Sample Tests")
#     def sample_tests():
#         test.assert_equals(sum_str("4","5"), "9")
#         test.assert_equals(sum_str("34","5"), "39")

#     @test.it("Tests with empty strings")
#     def empty_string():
#         test.assert_equals(sum_str("9",""), "9", "x + empty = x")
#         test.assert_equals(sum_str("","9"), "9", "empty + x = x")
#         test.assert_equals(sum_str("","") , "0", "empty + empty = 0")