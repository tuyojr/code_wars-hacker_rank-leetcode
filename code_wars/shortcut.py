# Create a function called shortcut to remove the lowercase vowels 
# (a, e, i, o, u ) in a given string.

# Examples
# "hello"     -->  "hll"
# "codewars"  -->  "cdwrs"
# "goodbye"   -->  "gdby"
# "HELLO"     -->  "HELLO"
# don't worry about uppercase vowels
# y is not considered a vowel for this kata

def shortcut( s ):
    # ...
    vowels = ('a', 'e', 'i', 'o', 'u')
    return ''.join([l for l in s if l not in vowels]);

# test.assert_equals(shortcut('hello'),'hll')
