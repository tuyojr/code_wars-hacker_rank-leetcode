# Given a string of digits, you should replace any digit below 
# 5 with '0' and any digit 5 and above with '1'. Return the 
# resulting string.

# Note: input will never be an empty string

def fake_bin(x):
    bin = []
    for i in x:
        bin.append(i)
    for j, item in enumerate(bin):
        if (int(item) < 5):
            bin[j] = '0'
        else:
            bin[j] = '1'
    return ''.join(bin)
    
# import codewars_test as test
# from solution import fake_bin

# @test.describe("Fixed Tests")
# def fixed_tests():
#     @test.it('Basic Test Cases')
#     def basic_test_cases():
#         tests = [
#             # [expected, input]
#             ["01011110001100111", "45385593107843568"],
#             ["101000111101101", "509321967506747"],
#             ["011011110000101010000011011", "366058562030849490134388085"],
#             ["01111100", "15889923"],
#             ["100111001111", "800857237867"],
#         ]
        
#         for exp, inp in tests:
#             test.assert_equals(fake_bin(inp), exp)