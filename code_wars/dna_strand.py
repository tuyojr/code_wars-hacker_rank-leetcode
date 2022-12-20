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

def DNA_strand(dna):
    # code here
    
    # create an empty string for the final base pair that accepts
    pair = ''
    
    # loop through each base in the DNA
    for base in dna:    
        
        # if the base is Adenine, pair it with the corresponding Thymine
        if base == 'A':
            pair += 'T'
            
        # if the base is Cytosine, pair it with the corresponding Guanine
        elif base == 'C':
            pair += 'G'
        
        # if the base is Thymine, pair it with the corresponding Adenine
        elif base == 'T':
            pair += 'A'
        
        # if the base is Guanine, pair it with the corresponding Cytosine
        else:
            pair += 'C'
    # return the corresponding updated base pair
    return pair

    # return dna.translate(str.maketrans("ATCG","TAGC"))
# import codewars_test as test
# from solution import DNA_strand

# @test.describe("Fixed Tests")
# def fixed_tests():
#     @test.it('Basic Test Cases')
#     def basic_test_cases():     
#         test.assert_equals(DNA_strand("AAAA"),"TTTT","String AAAA is")
#         test.assert_equals(DNA_strand("ATTGC"),"TAACG","String ATTGC is")
#         test.assert_equals(DNA_strand("GTAT"),"CATA","String GTAT is")