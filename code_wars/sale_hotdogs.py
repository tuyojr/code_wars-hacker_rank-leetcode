# In JavaScript, if..else is the most basic conditional statement, it consists of three 
# parts:condition, statement1, statement2, like this:

# if condition: statementa
# else:         statementb
# It means that if the condition is true, then execute the statementa, otherwise execute the 
# statementb. If the statementa or statementb are more than one line, you need to add { and } 
# at the head and tail of statements in JS, to keep the same indentation on Python and to put 
# an end in Ruby where it indeed ends.

# For example, if we want to judge whether a number is odd or even, we can write code like this:

# def odd_even(n):
#     if n % 2: return "odd number"
#     else:     return "even number"
# If there is more than one condition to judge, we can use the compound if...else statement. For example:

# def old_young(age):
#     if age < 16:        return "children"
#     elif age < 50:      return "young man" #use "else if" if needed
#     else:               return "old man"
# This function returns a different value depending on the parameter age.

# Looks very complicated? Well, JS and Ruby also support the ternary operator and Python has 
# something similar too:

# statementa if condition else statementb
# Condition and statement separated by "?", different statement separated by ":" in both Ruby and JS; 
# in Python you put the condition in the middle of two alternatives. The two examples above can be 
# simplified with ternary operator:

# def odd_even(n):
#     return "odd number" if n % 2 else "even number"
# def old_young(age):
#     return "children" if age < 16 else "young man" if age < 50 else "old man"
# Task:
# Complete function saleHotdogs/SaleHotDogs/sale_hotdogs, function accepts 1 parameter:n, n is the number 
#   of hotdogs a customer will buy, different numbers have different prices (refer to the following table), 
#   return how much money will the customer spend to buy that number of hotdogs.

# number of hotdogs	price per unit (cents)
# n < 5	100
# n >= 5 and n < 10	95
# n >= 10	90
# You can use if..else or ternary operator to complete it.

# When you have finished the work, click "Run Tests" to see if your code is working properly.

# In the end, click "Submit" to submit your code and pass this kata.




# import codewars_test as test
# from solution import sale_hotdogs

# @test.describe("Basic tests")
# def tests():
#     @test.it("Some examples")
#     def tests():
#         test.assert_equals(sale_hotdogs(0), 0)
#         test.assert_equals(sale_hotdogs(1), 100)
#         test.assert_equals(sale_hotdogs(2), 200)
#         test.assert_equals(sale_hotdogs(3), 300)
#         test.assert_equals(sale_hotdogs(4), 400)
#         test.assert_equals(sale_hotdogs(5), 475)
#         test.assert_equals(sale_hotdogs(9), 855)
#         test.assert_equals(sale_hotdogs(10), 900)
#         test.assert_equals(sale_hotdogs(11), 990)
#         test.assert_equals(sale_hotdogs(100), 9000)
