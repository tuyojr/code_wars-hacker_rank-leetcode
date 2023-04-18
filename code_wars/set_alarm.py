# Write a function named setAlarm which receives two parameters. The first parameter, 
# employed, is true whenever you are employed and the second parameter, vacation is 
# true whenever you are on vacation.

# The function should return true if you are employed and not on vacation (because 
#  these are the circumstances under which you need to set an alarm). It should return 
# false otherwise. Examples:

# setAlarm(true, true) -> false
# setAlarm(false, true) -> false
# setAlarm(false, false) -> false
# setAlarm(true, false) -> true



# import codewars_test as test
# from solution import set_alarm

# @test.describe("Fixed Tests")
# def fixed_tests():
#     @test.it('Basic Test Cases')
#     def basic_test_cases():
#         test.assert_equals(set_alarm(True, True), False, "Fails when input is True, True")
#         test.assert_equals(set_alarm(False, True), False, "Fails when input is False, True")
#         test.assert_equals(set_alarm(False, False), False, "Fails when input is False, False")
#         test.assert_equals(set_alarm(True, False), True, "Fails when input is True, False")
