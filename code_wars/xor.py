# Exclusive "or" (xor) Logical Operator
# Overview
# In some scripting languages like PHP, there exists a logical operator
# (e.g. &&, ||, and, or, etc.) called the "Exclusive Or" (hence the name
# of this Kata). The exclusive or evaluates two booleans. It then returns
# true if exactly one of the two expressions are true, false otherwise.
# For example:

# false xor false == false // since both are false
# true xor false == true // exactly one of the two expressions are true
# false xor true == true // exactly one of the two expressions are true
# true xor true == false // Both are true.  "xor" only returns true if EXACTLY
# one of the two expressions evaluate to true.
# Task
# Since we cannot define keywords in Javascript (well, at least I don't know
# how to do it), your task is to define a function xor(a, b) where a and b are
# the two expressions to be evaluated. Your xor function should have the behaviour
# described above, returning true if exactly one of the two expressions evaluate
# to true, false otherwise.

def xor(a,b):
    #your code here
    return True if ((a == True) and (b == False)) or ((a == False) and (b == True)) else False
    # return a != b

# import codewars_test as test
# from solution import xor

# @test.describe("Your 'xor' function/operator")
# def _():
    
#     @test.it("should work for the four basic cases described above")
#     def _():
#         test.assert_equals(xor(False, False), False, "False xor False == False")
#         test.assert_equals(xor(True, False), True, "True xor False == True")
#         test.assert_equals(xor(False, True), True, "False xor True == True")
        test.assert_equals(xor(True, True), False, "True xor True == False")