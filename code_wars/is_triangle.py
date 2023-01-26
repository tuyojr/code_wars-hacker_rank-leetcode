# Implement a function that accepts 3 integer values a, b, c. 
# The function should return true if a triangle can be built 
# with the sides of given length and false in any other case.

# (In this case, all triangles must have surface greater than 0 to be accepted).

def is_triangle(a, b, c):

    # check if the sum of any two sides is greater than the third side
    if a + b > c and a + c > b and b + c > a:

        # if so, check if any side is 0
        if a == 0 or b == 0 or c == 0:
            return False

        # if not, check if any side is negative
        elif a < 0 or b < 0 or c < 0:
            return False

        # if not, return True
        else:
            return True

    # if not, return False
    else:
        return False

# import codewars_test as test
# from solution import is_triangle

# @test.describe("Fixed Tests")
# def fixed_tests():
#     @test.it('Basic Test Cases')
#     def basic_test_cases():
#         test.assert_equals(is_triangle(1, 2, 2), True, "didn't work when sides were 1, 2, 2")
#         test.assert_equals(is_triangle(7, 2, 2), False, "didn't work when sides were 7, 2, 2")
#         test.assert_equals(is_triangle(1, 2, 3), False, "didn't work when sides were 1, 2, 3")
#         test.assert_equals(is_triangle(1, 3, 2), False, "didn't work when sides were 1, 3, 2")
#         test.assert_equals(is_triangle(3, 1, 2), False, "didn't work when sides were 3, 1, 2")
#         test.assert_equals(is_triangle(5, 1, 2), False, "didn't work when sides were 5, 1, 2")
#         test.assert_equals(is_triangle(1, 2, 5), False, "didn't work when sides were 1, 2, 5")
#         test.assert_equals(is_triangle(2, 5, 1), False, "didn't work when sides were 2, 5, 1")
#         test.assert_equals(is_triangle(4, 2, 3), True, "didn't work when sides were 4, 2, 3")
#         test.assert_equals(is_triangle(5, 1, 5), True, "didn't work when sides were 5, 1, 5")
#         test.assert_equals(is_triangle(2, 2, 2), True, "didn't work when sides were 2, 2, 2")
#         test.assert_equals(is_triangle(-1, 2, 3), False, "didn't work when sides were -1, 2, 3")
#         test.assert_equals(is_triangle(1, -2, 3), False, "didn't work when sides were 1, -2, 3")
#         test.assert_equals(is_triangle(1, 2, -3), False, "didn't work when sides were 1, 2, -3")
#         test.assert_equals(is_triangle(0, 2, 3), False, "didn't work when sides were 0, 2, 3")