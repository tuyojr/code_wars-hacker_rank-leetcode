# A deque is a double-ended queue. It can be used to add or 
# remove elements from both ends.

# Deques support thread safe, memory efficient appends and 
# pops from either side of the deque with approximately the 
# same O(1) performance in either direction.

# Click on the link to learn more about deque() methods 
# (https://docs.python.org/2/library/collections.html#deque-objects).
# Click on the link to learn more about various approaches to 
# working with deques: Deque Recipes (https://docs.python.org/2/library/collections.html#deque-objects).

# Example

# Code
# >>> from collections import deque
# >>> d = deque()
# >>> d.append(1)
# >>> print d
# deque([1])
# >>> d.appendleft(2)
# >>> print d
# deque([2, 1])
# >>> d.clear()
# >>> print d
# deque([])
# >>> d.extend('1')
# >>> print d
# deque(['1'])
# >>> d.extendleft('234')
# >>> print d
# deque(['4', '3', '2', '1'])
# >>> d.count('1')
# 1
# >>> d.pop()
# '1'
# >>> print d
# deque(['4', '3', '2'])
# >>> d.popleft()
# '4'
# >>> print d
# deque(['3', '2'])
# >>> d.extend('7896')
# >>> print d
# deque(['3', '2', '7', '8', '9', '6'])
# >>> d.remove('2')
# >>> print d
# deque(['3', '7', '8', '9', '6'])
# >>> d.reverse()
# >>> print d
# deque(['6', '9', '8', '7', '3'])
# >>> d.rotate(3)
# >>> print d
# deque(['8', '7', '3', '6', '9'])

# Task
# Perform append, pop, popleft and appendleft methods on an empty deque d.

# Input Format
# The first line contains an integer N, the number of operations.
# The next N lines contains the space separated names of methods and their values.

# Constraints
# 0 < N <= 100

# Output Format
# Print the space separated elements of deque d.

# Sample Input
# 6
# append 1
# append 2
# append 3
# appendleft 4
# pop
# popleft

# Sample Output
# 1 2

# Enter your code here. Read input from STDIN. Print output to STDOUT

# import the deque module
from collections import deque

# prompt the user for the number of values they want to input
N = int(input())

# create an empty list to hold the methods input by the user
methods = []

# loop through each method and add them to the list
for i in range(N):
    methods.append(input())

# use the deque module to create an empty deque
d = deque()

# loop through each method in the list
for items in methods:
    
    try:
        # try to append each method and value to a variable
        method, value = items.split(' ')
        
        # use eval method to exectue a method input by the user on the deque
        eval('d.{}({})'.format(method, value))
    
    except:
        # use the except method to execute user methods that have no value    
        eval('d.{}()'.format(items))
        
# loop through each value in the deque and print them to the screen
for num in d:
    print(num, end=' ')
    