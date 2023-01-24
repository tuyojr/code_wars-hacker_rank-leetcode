# A.difference(B) or A -B 

# .difference()
# The tool .difference() returns a set with all the elements from the set 
# that are not in an iterable.
# Sometimes the - operator is used in place of the .difference() tool, but 
# it only operates on the set of elements in set.
# Set is immutable to the .difference() operation (or the - operation).

# >>> s = set("Hacker")
# >>> print s.difference("Rank")
# set(['c', 'r', 'e', 'H'])

# >>> print s.difference(set(['R', 'a', 'n', 'k']))
# set(['c', 'r', 'e', 'H'])

# >>> print s.difference(['R', 'a', 'n', 'k'])
# set(['c', 'r', 'e', 'H'])

# >>> print s.difference(enumerate(['R', 'a', 'n', 'k']))
# set(['a', 'c', 'r', 'e', 'H', 'k'])

# >>> print s.difference({"Rank":1})
# set(['a', 'c', 'e', 'H', 'k', 'r'])

# >>> s - set("Rank")
# set(['H', 'c', 'r', 'e'])

# Task
# The students of District College have subscriptions to English and 
# French newspapers. Some students have subscribed only to English, 
# some have subscribed only to French, and some have subscribed to 
# both newspapers.

# You are given two sets of student roll numbers. One set has subscribed 
# to the English newspaper, one set has subscribed to the French newspaper. 
# Your task is to find the total number of students who have subscribed to 
# both newspapers.

# Input Format

# The first line contains n, the number of students who have subscribed to 
# the English newspaper.
# The second line contains n space separated roll numbers of those students.
# The third line contains b, the number of students who have subscribed to 
# the French newspaper.
# The fourth line contains b space separated roll numbers of those students.

# Constraints
# 0 < Total number of students in college < 1000

# Output Format

# Output the total number of students who have subscriptions to both English 
# and French newspapers.

# Sample Input

# 9
# 1 2 3 4 5 6 7 8 9
# 9
# 10 1 2 3 11 21 55 6 8

# Sample Output

# 4

# Explanation

# The roll numbers of students who have both subscriptions:
# 1, 2, 3, 6 and 8.
# Hence, the total is 5 students.

# Enter your code here. Read input from STDIN. Print output to STDOUT

if __name__ == '__main__':
    
    # number of students subscribed to English papers
    n = int(input())
    
    # students subscribed to english papers
    english = set(map(int, input(). split()))
    
    # number of students subscribed to French papers
    b = int(input())
    
    # students subscribed to french papers
    french = set(map(int, input(). split()))

    print(len(english.difference(french)))