# Make a program that filters a list of strings and returns 
# a list with only your friends name in it.

# If a name has exactly 4 letters in it, you can be sure that 
# it has to be a friend of yours! Otherwise, you can be sure he's not...

# Ex: Input = ["Ryan", "Kieran", "Jason", "Yous"], Output = ["Ryan", "Yous"]

# i.e.

# friend ["Ryan", "Kieran", "Mark"] `shouldBe` ["Ryan", "Mark"]
# Note: keep the original order of the names in the output.



# import codewars_test as test
# from solution import friend

# @test.describe("Fixed Tests")
# def fixed_tests():
#     @test.it('Sample Test Cases')
#     def sample_test_cases():
#         test.assert_equals(friend(["Ryan", "Kieran", "Mark",]), ["Ryan", "Mark"])
#         test.assert_equals(friend(["Ryan", "Jimmy", "123", "4", "Cool Man"]), ["Ryan"])
#         test.assert_equals(friend(["Jimm", "Cari", "aret", "truehdnviegkwgvke", "sixtyiscooooool"]), ["Jimm", "Cari", "aret"])