# You are given a string S.
# S contains alphanumeric characters only.
# Your task is to sort the string S in the following manner:

# - All sorted lowercase letters are ahead of uppercase letters.
# - All sorted uppercase letters are ahead of digits.
# - All sorted odd digits are ahead of sorted even digits.

# Input Format

# A single line of input contains the string S.

# Constraints

# 0 < len(S) < 1000

# Output Format

# Output the sorted string S.

# Sample Input

# Sorting1234

# Sample Output

# ginortS1324

# Enter your code here. Read input from STDIN. Print output to STDOUT

def sort_string(string):

    # create a list for all the lowercase letters
    lower = []

    # create a list for all the uppercase letters
    upper = []

    # create a list for all the odd numbers
    odd = []

    # create a list for all the even numbers
    even = []

    # iterate through the string
    for i in string:

        # if the character is lowercase, add it to the lower list
        if i.islower():
            lower.append(i)

        # if the character is uppercase, add it to the upper list
        elif i.isupper():
            upper.append(i)

        # if the character is an odd number, add it to the odd list
        elif int(i) % 2 == 0:
            even.append(i)

        # if the character is an even number, add it to the even list
        else:
            odd.append(i)

    # sort the lists
    lower.sort()
    upper.sort()
    odd.sort()
    even.sort()

    # return the sorted string in the required order
    return ''.join(lower + upper + odd + even)

if __name__ == '__main__':
    s = input()
    print(sort_string(s))