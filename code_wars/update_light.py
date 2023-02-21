# You're writing code to control your town's traffic lights. 
# You need a function to handle each change from green, to 
# yellow, to red, and then to green again.

# Complete the function that takes a string as an argument 
# representing the current state of the light and returns a 
# string representing the state the light should change to.

# For example, when the input is green, output should be yellow.

def update_light(current):
    # Your code here.
    if current == 'yellow':
        return 'red'
    elif current == 'green':
        return 'yellow'
    else:
        return 'green'
    
    # other solution
    # return {"green": "yellow", "yellow": "red", "red": "green"}[current]

# import codewars_test as test
# from solution import update_light

# @test.describe("Fixed Tests")
# def fixed_tests():
#     @test.it('Basic Test Cases')
#     def basic_test_cases():
#         test.assert_equals(update_light('green'), 'yellow')
#         test.assert_equals(update_light('yellow'), 'red')
#         test.assert_equals(update_light('red'), 'green')