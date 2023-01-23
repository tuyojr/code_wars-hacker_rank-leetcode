# The itertools module standardizes a core set of fast, memory efficient 
# tools that are useful by themselves or in combination. Together, they 
# form an iterator algebra making it possible to construct specialized 
# tools succinctly and efficiently in pure Python.

# To read more about the functions in this module, check out their documentation 
# here. https://docs.python.org/3/library/itertools.html

# You are given a list of N lowercase English letters. For a given integer K, 
# you can select any K indices (assume 1-based indexing) with a uniform probability 
# from the list.

# Find the probability that at least one of the K indices selected will contain the 
# letter: 'a'.

# Input Format

# The input consists of three lines. The first line contains the integer N, 
# denoting the length of the list. The next line consists of N space-separated 
# lowercase English letters, denoting the elements of the list.

# The third and the last line of input contains the integer K, denoting the 
# number of indices to be selected.

# Output Format

# Output a single line consisting of the probability that at least one of the K 
# indices selected contains the letter:'a'.

# Note: The answer must be correct up to 3 decimal places.

# Constraints
# 1 <= N <= 10
# 1 <= K <= N

# All the letters in the list are lowercase English letters.

# Sample Input

# 4 
# a a c d
# 2

# Sample Output

# 0.8333

# Explanation

# All possible unordered tuples of length 2 comprising of indices from 1 to 4 are:


# Out of these 6 combinations, 5 of them contain either index 1 or index 2 which are 
# the indices that contain the letter 'a'.

# Hence, the answer is 5/6.

# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations

if __name__ == '__main__':

    # prompt the user for the number of letters in the list
    N = int(input())

    # prompt the user for the list of letters
    a = input().split()

    # prompt the user for the number of indices to be selected
    K = int(input())

    # create a count variable for the number of letters we're looking out for in the list
    count = 0

    # iterate through the list of letters and count the number of times the letter 'a' appears
    for i in combinations(a, K):
        if 'a' in i:
            count += 1

    # print the probability that at least one of the K indices selected contains the letter:'a'    
    print(count/len(list(combinations(a, K))))