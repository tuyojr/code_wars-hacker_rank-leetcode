# Count the number of divisors of a positive integer n.

# Random tests go up to n = 500000.

# Examples (input --> output)
# 4 --> 3 (1, 2, 4)
# 5 --> 2 (1, 5)
# 12 --> 6 (1, 2, 3, 4, 6, 12)
# 30 --> 8 (1, 2, 3, 5, 6, 10, 15, 30)
# Note you should only return a number, the count of divisors. 
# The numbers between parentheses are shown only for you to see 
# which numbers are counted in each case.

def divisors(n):
    
    # create a list to hold each possible divisor
    divisor = []
    
    # loop through the range of numbers from 1 to the value of n + 1
    for i in range(1, n + 1):
        
        # if the number can divide n without a remainder, add it to the list
        if n % i == 0:
            divisor.append(i)
            
    # return the list of divisors
    return len(divisor)

    # one line code
    # return len([i for i in range(1, n + 1) if n % i == 0])

# import codewars_test as test
# from solution import divisors

# @test.describe("Fixed Tests")
# def fixed_tests():
#     @test.it('Basic Test Cases')
#     def basic_test_cases():
#         test.assert_equals(divisors(1), 1) 
#         test.assert_equals(divisors(4), 3)
#         test.assert_equals(divisors(5), 2)
#         test.assert_equals(divisors(12), 6)
#         test.assert_equals(divisors(30), 8)
#         test.assert_equals(divisors(4096), 13)