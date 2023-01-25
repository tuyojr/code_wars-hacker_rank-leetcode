# The number 
# 89
# 89 is the first integer with more than one digit that fulfills the 
# property partially introduced in the title of this kata. What's 
# the use of saying "Eureka"? Because this sum gives the same number: 
# 89 = 8^1 + 9^2 

# The next number in having this property is 135:

# See this property again: 135 = 1^1 + 3^2 + 5^3 

# Task
# We need a function to collect these numbers, that may receive two integers a, b 
# that defines the range[a,b] (inclusive) and outputs a list of the sorted numbers 
# in the range that fulfills the property described above.

# Examples
# Let's see some cases (input -> output):

# 1, 10  --> [1, 2, 3, 4, 5, 6, 7, 8, 9]
# 1, 100 --> [1, 2, 3, 4, 5, 6, 7, 8, 9, 89]

# If there are no numbers of this kind in the range[a,b] the function should output 
# an empty list.

# 90, 100 --> []

# Enjoy it!!

def sum_dig_pow(a, b): # range(a, b + 1) will be studied by the function
    # your code here

    # create a list of numbers in the range
    num_list = list(range(a, b + 1))

    # create a list to hold the numbers that meet the criteria
    sum_list = []

    # loop through the list of numbers
    for num in num_list:

        # convert the number to a string
        num_str = str(num)

        # create a list to hold the digits of the number
        num_digits = []

        # loop through the string and add the digits to the list
        for digit in num_str:
            num_digits.append(int(digit))

        # create a list to hold the sum of the digits raised to the power of their index
        sum_digits = []

        # loop through the digits and raise them to the power of their index
        for i in range(len(num_digits)):
            sum_digits.append(num_digits[i] ** (i + 1))

        # if the sum of the digits raised to the power of their index equals the number
        # add the number to the sum_list
        if sum(sum_digits) == num:
            sum_list.append(num)
        
    return sum_list
    # return [x for x in range(a, b+1) if sum(int(d)**i for i, d in enumerate(str(x), 1)) == x]

# from solution import sum_dig_pow
# import codewars_test as test

# @test.describe("Take a Number And Sum Its Digits Raised To The Consecutive Powers And ....¡Eureka!!")
# def desc1():
#     @test.it('Sample tests')
#     def it1():
#         test.assert_equals( sum_dig_pow(1, 10), [1, 2, 3, 4, 5, 6, 7, 8, 9])
#         test.assert_equals(sum_dig_pow(1, 100), [1, 2, 3, 4, 5, 6, 7, 8, 9, 89])
#         test.assert_equals(sum_dig_pow(10, 89),  [89])
#         test.assert_equals(sum_dig_pow(10, 100),  [89])
#         test.assert_equals(sum_dig_pow(90, 100), [])
#         test.assert_equals(sum_dig_pow(89, 135), [89, 135])