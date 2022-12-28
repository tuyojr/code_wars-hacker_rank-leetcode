# Jaden Smith, the son of Will Smith, is the star of films such as 
# The Karate Kid (2010) and After Earth (2013). Jaden is also known 
# for some of his philosophy that he delivers via Twitter
# https://twitter.com/jaden. 
# When writing on Twitter, he is known for almost always capitalizing 
# every word. For simplicity, you'll have to capitalize each word, 
# check out how contractions are expected to be in the example below.

# Your task is to convert strings to how they would be written by Jaden Smith. 
# The strings are actual quotes from Jaden Smith, but they are not capitalized 
# in the same way he originally typed them.

# Example:
# Not Jaden-Cased: "How can mirrors be real if our eyes aren't real"
# Jaden-Cased:     "How Can Mirrors Be Real If Our Eyes Aren't Real"

# Link to Jaden's former Twitter account @officialjaden via archive.org
# https://web.archive.org/web/20190624190255/https://twitter.com/officialjaden

def to_jaden_case(string):
    # ...
    # use a list comprehension to split the quote into words and capitalize 
    # the first letter iin each and join them back.
    return " ".join([w.capitalize() for w in string.split()])

# from solution import to_jaden_case
# import codewars_test as test


# @test.describe('Sample test')
# def basic_tests():
#     @test.it('Simple text')
#     def _():
#         quote = "How can mirrors be real if our eyes aren't real"
#         test.assert_equals(to_jaden_case(quote), "How Can Mirrors Be Real If Our Eyes Aren't Real")