# The main idea is to count all the occurring characters in a string. If you 
# have a string like aba, then the result should be {'a': 2, 'b': 1}.

# What if the string is empty? Then the result should be empty object literal, {}.

def count(s):
    # The function code should be here
    count = dict()
    
    for letter in s:
        if s != None:
            count[letter] = count.get(letter, 0) + 1
        else:
            return {}
    return count

# import codewars_test as test
# from solution import count

# @test.describe("Basic Tests")
# def basic_tests():
    
#     @test.it("Basic Tests")
#     def basic_tests():
#         test.assert_equals(count('aba'), {'a': 2, 'b': 1})
#         test.assert_equals(count(''), {})
#         test.assert_equals(count('aa'), {'a' : 2})
#         test.assert_equals(count('aabb'), {'b' : 2, 'a' : 2})
