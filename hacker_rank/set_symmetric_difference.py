# A.symmetric_difference(B) or A^B

# .symmetric_difference()
# The .symmetric_difference() operator returns a set with all the 
# elements that are in the set and the iterable but not both.
# Sometimes, a ^ operator is used in place of the .symmetric_difference() 
# tool, but it only operates on the set of elements in set.
# The set is immutable to the .symmetric_difference() operation (or ^ operation).

# >>> s = set("Hacker")
# >>> print s.symmetric_difference("Rank")
# set(['c', 'e', 'H', 'n', 'R', 'r'])

# >>> print s.symmetric_difference(set(['R', 'a', 'n', 'k']))
# set(['c', 'e', 'H', 'n', 'R', 'r'])

# >>> print s.symmetric_difference(['R', 'a', 'n', 'k'])
# set(['c', 'e', 'H', 'n', 'R', 'r'])

# >>> print s.symmetric_difference(enumerate(['R', 'a', 'n', 'k']))
# set(['a', 'c', 'e', 'H', (0, 'R'), 'r', (2, 'n'), 'k', (1, 'a'), (3, 'k')])

# >>> print s.symmetric_difference({"Rank":1})
# set(['a', 'c', 'e', 'H', 'k', 'Rank', 'r'])

# >>> s ^ set("Rank")
# set(['c', 'e', 'H', 'n', 'R', 'r'])

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

# 8

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

    print(len(english^french))