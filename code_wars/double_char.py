# Given a string, you have to return a string in which each 
# character (case-sensitive) is repeated once.

# Examples (Input -> Output):
# * "String"      -> "SSttrriinngg"
# * "Hello World" -> "HHeelllloo  WWoorrlldd"
# * "1234!_ "     -> "11223344!!__  "
# Good Luck!

def double_char(s):
    
    # create an empty string variable for the final result
    result = ''
    
    # loop through each character in the string
    for char in s:
        
        # for each character in the the string, update the result twice each time
        result += char + char
    
    # return the result
    return result

# test.assert_equals(double_char("String"),"SSttrriinngg")
# test.assert_equals(double_char("Hello World"),"HHeelllloo  WWoorrlldd")
# test.assert_equals(double_char("1234!_ "),"11223344!!__  ")
