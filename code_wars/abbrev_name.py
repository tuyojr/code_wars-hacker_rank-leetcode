# Write a function to convert a name into initials. This kata strictly 
# takes two words with one space in between them.

# The output should be two capital letters with a dot separating them.

# It should look like this:

# Sam Harris => S.H

# patrick feeney => P.F

def abbrev_name(name):
    names = [i for i in name.split(' ')]
    return f'{names[0][0].upper()}.{names[1][0].upper()}'

# import codewars_test as test

# try:
#     from solution import abbrevName as abbrev_name
# except ImportError:
#     from solution import abbrev_name

# @test.describe("Fixed Tests")
# def basic_tests():
#     @test.it('Basic Test Cases')
#     def basic_test_cases():
#         test.assert_equals(abbrev_name("Sam Harris"), "S.H")
#         test.assert_equals(abbrev_name("patrick feenan"), "P.F")
#         test.assert_equals(abbrev_name("Evan C"), "E.C")
#         test.assert_equals(abbrev_name("P Favuzzi"), "P.F")
#         test.assert_equals(abbrev_name("David Mendieta"), "D.M")