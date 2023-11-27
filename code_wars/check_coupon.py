# Story
# Your online store likes to give out coupons for special occasions. 
# Some customers try to cheat the system by entering invalid codes or 
# using expired coupons.

# Task
# Your mission:
# Write a function called checkCoupon which verifies that a coupon code 
# is valid and not expired.

# A coupon is no more valid on the day AFTER the expiration date. 
# All dates will be passed as strings in this format: "MONTH DATE, YEAR"

from datetime import datetime

def check_coupon(entered_code, correct_code, current_date, expiration_date):
    current_date_formatted = datetime.strptime(current_date, "%B %d, %Y")
    expiration_date_formatted = datetime.strptime(current_date, "%B %d, %Y")
    return entered_code is correct_code and expiration_date_formatted >= current_date_formatted

# from solution import check_coupon
# import codewars_test as test

# @test.it("Example tests")
# def example_tests():
#     test.assert_equals(check_coupon('123','123','September 5, 2014','October 1, 2014'), True);
#     test.assert_equals(check_coupon('123a','123','September 5, 2014','October 1, 2014'), False);