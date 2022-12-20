# Deoxyribonucleic acid (DNA) is a chemical found in the nucleus of 
# cells and carries the "instructions" for the development and 
# functioning of living organisms.

# If you want to know more: http://en.wikipedia.org/wiki/DNA

# In DNA strings, symbols "A" and "T" are complements of each other, 
# as "C" and "G". Your function receives one side of the DNA (string, 
# except for Haskell); you need to return the other complementary side. 
# DNA strand is never empty or there is no DNA at all (again, except for 
# Haskell).

# More similar exercise are found here: http://rosalind.info/problems/list-view/ 
# (source)

# Example: (input --> output)

# "ATTGC" --> "TAACG"
# "GTAT" --> "CATA"




# import codewars_test as test
# from solution import DNA_strand

# @test.describe("Fixed Tests")
# def fixed_tests():
#     @test.it('Basic Test Cases')
#     def basic_test_cases():     
#         test.assert_equals(DNA_strand("AAAA"),"TTTT","String AAAA is")
#         test.assert_equals(DNA_strand("ATTGC"),"TAACG","String ATTGC is")
#         test.assert_equals(DNA_strand("GTAT"),"CATA","String GTAT is")