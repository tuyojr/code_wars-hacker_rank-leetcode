# Kids drink toddy.
# Teens drink coke.
# Young adults drink beer.
# Adults drink whisky.
# Make a function that receive age, and return what they drink.

# Rules:

# Children under 14 old.
# Teens under 18 old.
# Young under 21 old.
# Adults have 21 or more.
# Examples: (Input --> Output)

# 13 --> "drink toddy"
# 17 --> "drink coke"
# 18 --> "drink beer"
# 20 --> "drink beer"
# 30 --> "drink whisky"

def people_with_age_drink(age):
    if age < 14:
        return 'drink toddy'
    elif age < 18:
        return 'drink coke'
    elif age < 21:
        return 'drink beer'
    elif age >= 21:
        return 'drink whisky'

# import codewars_test as test
# from solution import people_with_age_drink

# @test.describe("Fixed Tests")
# def fixed_tests():
#     @test.it("should return 'drink toddy' when age is less than 14")
#     def _():
#         test.assert_equals(people_with_age_drink(13), 'drink toddy', "Wrong result for 13")
#         test.assert_equals(people_with_age_drink(0), 'drink toddy', "Wrong result for 0")

#     @test.it("should return 'drink coke' when age is between 14(inclusive) and 18(exclusive)")
#     def _():
#         test.assert_equals(people_with_age_drink(17), 'drink coke')
#         test.assert_equals(people_with_age_drink(15), 'drink coke')
#         test.assert_equals(people_with_age_drink(14), 'drink coke')

#     @test.it("should return 'drink beer' when age is between 18(inclusive) and 21(exclusive)")
#     def _():
#         test.assert_equals(people_with_age_drink(20), 'drink beer')
#         test.assert_equals(people_with_age_drink(18), 'drink beer')

#     @test.it("should return 'drink whisky' when age is greater than or equal to 21")
#     def _():
#         test.assert_equals(people_with_age_drink(22), 'drink whisky')
#         test.assert_equals(people_with_age_drink(21), 'drink whisky')
