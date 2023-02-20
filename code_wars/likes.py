# You probably know the "like" system from Facebook and other pages. 
# People can "like" blog posts, pictures or other items. We want to 
# create the text that should be displayed next to such an item.

# Implement the function which takes an array containing the names of 
# people that like an item. It must return the display text as shown 
# in the examples:

# []                                -->  "no one likes this"
# ["Peter"]                         -->  "Peter likes this"
# ["Jacob", "Alex"]                 -->  "Jacob and Alex like this"
# ["Max", "John", "Mark"]           -->  "Max, John and Mark like this"
# ["Alex", "Jacob", "Mark", "Max"]  -->  "Alex, Jacob and 2 others like this"
# Note: For 4 or more names, the number in "and 2 others" simply increases.

def likes(names):
    # your code here
    if len(names) == 0:
        return "no one likes this"
    elif len(names) == 1:
        return names[0] + " likes this"
    elif len(names) == 2:
        return names[0] + " and " + names[1] + " like this"
    elif len(names) == 3:
        return names[0] + ", " + names[1] + " and " + names[2] + " like this"
    else:
        return names[0] + ", " + names[1] + " and " + str(len(names) - 2) + " others like this"

# import codewars_test as test
# from solution import likes

# @test.it('Basic tests')
# def _():
#     test.assert_equals(likes([]), 'no one likes this')
#     test.assert_equals(likes(['Peter']), 'Peter likes this')
#     test.assert_equals(likes(['Jacob', 'Alex']), 'Jacob and Alex like this')
#     test.assert_equals(likes(['Max', 'John', 'Mark']), 'Max, John and Mark like this')
#     test.assert_equals(likes(['Alex', 'Jacob', 'Mark', 'Max']), 'Alex, Jacob and 2 others like this')