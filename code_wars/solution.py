# Complete the solution so that the function will break up camel casing, 
# using a space between words.

# Example
# "camelCasing"  =>  "camel Casing"
# "identifier"   =>  "identifier"
# ""             =>  ""

def solution(s):
    result = ""
    for letter in s:
        if letter != letter.upper():
            result += letter
        elif letter == letter.upper():
            result += " " + letter
    return result

# test.assert_equals(solution("helloWorld"), "hello World")
# test.assert_equals(solution("camelCase"), "camel Case")
# test.assert_equals(solution("breakCamelCase"), "break Camel Case")
