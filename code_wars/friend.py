# Make a program that filters a list of strings and returns 
# a list with only your friends name in it.

# If a name has exactly 4 letters in it, you can be sure that 
# it has to be a friend of yours! Otherwise, you can be sure he's not...

# Ex: Input = ["Ryan", "Kieran", "Jason", "Yous"], Output = ["Ryan", "Yous"]

# i.e.

# friend ["Ryan", "Kieran", "Mark"] `shouldBe` ["Ryan", "Mark"]
# Note: keep the original order of the names in the output.

def friend(x):
    # create an empty list to hold your list of friends
    friends = []
    
    # loop through the input list of potential friends
    for i in x:
        
        # create a variable to hold the list of each friend, separated by a comma
        # in the original list.
        f = i.split(',')
        
        # loop through each person's name
        for name in f:
            
            # if the name is exactly 4 characters, we want to add them to our friend's
            # list
            if len(name) == 4:
                friends.append(name)
    
    # return the friends list
    return friends
    # return [f for f in x if len(f) == 4]

# import codewars_test as test
# from solution import friend

# @test.describe("Fixed Tests")
# def fixed_tests():
#     @test.it('Sample Test Cases')
#     def sample_test_cases():
#         test.assert_equals(friend(["Ryan", "Kieran", "Mark",]), ["Ryan", "Mark"])
#         test.assert_equals(friend(["Ryan", "Jimmy", "123", "4", "Cool Man"]), ["Ryan"])
#         test.assert_equals(friend(["Jimm", "Cari", "aret", "truehdnviegkwgvke", "sixtyiscooooool"]), ["Jimm", "Cari", "aret"])