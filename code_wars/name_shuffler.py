# Write a function that returns a string in which firstname is swapped with last name.

# Example(Input --> Output)

# "john McClane" --> "McClane john"

def name_shuffler(str_):
    #your code here
    new_str = str_.split()
    return new_str[1] + " " + new_str[0]

# import codewars_test as test
# from solution import name_shuffler

# @test.describe("Fixed Tests")
# def fixed_tests():
#     @test.it('Basic Test Cases')
#     def basic_test_cases():
#         test.assert_equals(name_shuffler('john McClane'),'McClane john')
#         test.assert_equals(name_shuffler('Mary jeggins'),'jeggins Mary')
#         test.assert_equals(name_shuffler('tom jerry'),'jerry tom')