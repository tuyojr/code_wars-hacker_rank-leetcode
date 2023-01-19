# Return the number (count) of vowels in the given string.

# We will consider a, e, i, o, u as vowels for this Kata (but not y).

# The input string will only consist of lower case letters and/or spaces.

def get_count(sentence):
    
    # create a count variable for the vowels in the sentence
    num_vowels = 0
    
    # create a list of possible vowels
    vowels = ['a', 'e', 'i', 'o', 'u']
    
    # loop through each letter in the sentence
    for char in sentence:
        
        # if the lette is in the vowels list, update the count variable
        if char in vowels:
            num_vowels += 1
    
    # return the total variable count
    return num_vowels

# import codewars_test as test
# from solution import get_count

# @test.describe("Sample tests")
# def sample_tests():
    
#     @test.it("Should count all vowels")
#     def all_vowels():
#         test.assert_equals(get_count("aeiou"), 5, f"Incorrect answer for \"aeiou\"")
        
#     @test.it("Should not count \"y\"")
#     def only_y():
#         test.assert_equals(get_count("y"), 0, f"Incorrect answer for \"y\"")        
        
#     @test.it("Should return 0 when no vowels")
#     def no_vowels():
#         test.assert_equals(get_count("bcdfghjklmnpqrstvwxz y"), 0, f"Incorrect answer for \"bcdfghjklmnpqrstvwxz y\"")
        
#     @test.it("Should return 0 for empty string")
#     def no_vowels():
#         test.assert_equals(get_count(""), 0, f"Incorrect answer for empty string")
        
#     @test.it("Should return 5 for \"abracadabra\"")
#     def test_abracadabra():    
#         test.assert_equals(get_count("abracadabra"), 5, f"Incorrect answer for \"abracadabra\"")