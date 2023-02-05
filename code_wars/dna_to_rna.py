# Deoxyribonucleic acid, DNA is the primary information storage 
# molecule in biological systems. It is composed of four nucleic 
# acid bases Guanine ('G'), Cytosine ('C'), Adenine ('A'), and 
# Thymine ('T').

# Ribonucleic acid, RNA, is the primary messenger molecule in cells. 
# RNA differs slightly from DNA its chemical structure and contains 
# no Thymine. In RNA Thymine is replaced by another nucleic acid 
# Uracil ('U').

# Create a function which translates a given DNA string into RNA.

# For example:

# "GCAT"  =>  "GCAU"
# The input string can be of arbitrary length - in particular, it may 
# be empty. All input is guaranteed to be valid, i.e. each input string 
# will only ever consist of 'G', 'C', 'A' and/or 'T'.

def dna_to_rna(dna):
    # create a list of dna bases
    dna_list = list(dna)

    # create a list of rna bases
    rna_list = []

    # loop through the list of dna bases
    for base in dna_list:

        # if the base is a 'T', replace it with an 'U'
        if base == 'T':
            rna_list.append('U')

        # otherwise, append the base to the list of rna bases
        else:
            rna_list.append(base)

    # join the list of rna bases into a string
    rna = ''.join(rna_list)

    # return the string of rna bases
    return rna

    # one line solution
    # return dna.replace('T', 'U')

# import codewars_test as test
# from solution import dna_to_rna

# @test.describe("Sample Tests")
# def basic_tests():
#     @test.it('Basic Test Cases')
#     def basic_test_cases():
#         test.assert_equals(dna_to_rna("TTTT"), "UUUU")
#         test.assert_equals(dna_to_rna("GCAT"), "GCAU")
#         test.assert_equals(dna_to_rna("GACCGCCGCC"), "GACCGCCGCC")