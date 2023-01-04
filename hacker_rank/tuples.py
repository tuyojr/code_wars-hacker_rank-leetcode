# Task
# Given an integer, n, and n space-separated integers as input, 
# create a tuple, t, of those n integers. Then compute and print 
# the result of hash(t).

# Note: hash() is one of the functions in the __builtins__ module, 
# so it need not be imported.

# Input Format
# The first line contains an integer, n, denoting the number of 
# elements in the tuple.
# The second line contains n space-separated integers describing the 
# elements in tuple t.

# Output Format
# Print the result of hash(t).

# Sample Input 0
# 2
# 1 2

# Sample Output 0
# 3713081631934410656

# Enter your code here. Read input from STDIN. Print output to STDOUT
# Pypy3
if __name__ == '__main__':

    # prompt the user for the number of input
    n = int(input())

    # create the n-space separated integers
    integer_list = map(int, input().split())

    # create a tuple from the input integers
    t = tuple(integer_list)

    # compute and print the result of the hash
    print(hash(t))