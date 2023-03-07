# Terminal game move function
# In this game, the hero moves from left to right. The player rolls the dice 
# and moves the number of spaces indicated by the dice two times.

# Create a function for the terminal game that takes the current position of 
# the hero and the roll (1-6) and return the new position.

# Example:
# move(3, 6) should equal 15

def move(position, roll):
    # your code here
    return position + (roll * 2)

# import codewars_test as test
# from solution import move

# @test.describe("Fixed Tests")
# def fixed_tests():
#     @test.it('Basic Test Cases')
#     def basic_test_cases():
#         test.assert_equals(move(0, 4), 8)
#         test.assert_equals(move(3, 6), 15)
#         test.assert_equals(move(2, 5), 12)
