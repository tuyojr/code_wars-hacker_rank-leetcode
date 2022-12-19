# You are given n words. Some words may repeat. For each word, output 
# its number of occurrences. The output order should correspond with the 
# input order of appearance of the word. See the sample input/output for 
# clarification.

# Note: Each input line ends with a "\n" character.

# Constraints:
# 1 <= n <= 10^5

# The sum of the lengths of all the words do not exceed 10^6
# All the words are composed of lowercase English letters only.

# Input Format

# The first line contains the integer, n.
# The next n lines each contain a word.

# Output Format

# Output 2 lines.
# On the first line, output the number of distinct words from the input.
# On the second line, output the number of occurrences for each distinct 
# word according to their appearance in the input.

# Sample Input
# 4
# bcdef
# abcdefg
# bcde
# bcdef

# Sample Output
# 3
# 2 1 1
# Explanation

# There are 3 distinct words. Here, "bcdef" appears twice in the input 
# at the first and last positions. The other words appear once each. 
# The order of the first appearances are "bcdef", "abcdefg" and "bcde" 
# which corresponds to the output.

# prompt the user to enter the total number of times they want to input a word
n = int(input())

# create an empty dictionary to store the words and the number of occurrences
word_dict = dict()

# create a count variable to track the total number of words in the dictionary
total_words = 0

# loop through the words the number of times the user entered
for word in range(n):

    # create a list to store the words and makes sure they're all in lower 
    # case and the \n character is removed
    words_list = input().lower().rstrip()

    # each time the loop runs, store the word from the word list as a key in 
    # the dictionary if it's not already there if it is there, it just 
    # increases the value of the key
    word_dict[words_list] = word_dict.get(words_list, 0) + 1

    # set the count variable to the number of words in the dictionary
    total_words = len(word_dict)

# output the count variable
print(total_words)

# create an empty list to hold only the values of the dictionary
values = list()

# loop through all the words (keys) in the dictionary an update the list with the values
for key, value in word_dict.items():
    values.append(value)

# since there can be a variable amount of user input, meaning a word can occur any number of times
# we can print the values in the list using the '*values' and separate them with a space.
print(*values, sep=' ')