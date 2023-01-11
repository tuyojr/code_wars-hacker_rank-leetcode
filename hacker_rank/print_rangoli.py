# You are given an integer, N. Your task is to print an alphabet 
# rangoli of size N. (Rangoli is a form of Indian folk art based on 
# creation of patterns.)

# Different sizes of alphabet rangoli are shown below:

# #size 3

# ----c----
# --c-b-c--
# c-b-a-b-c
# --c-b-c--
# ----c----

# #size 5

# --------e--------
# ------e-d-e------
# ----e-d-c-d-e----
# --e-d-c-b-c-d-e--
# e-d-c-b-a-b-c-d-e
# --e-d-c-b-c-d-e--
# ----e-d-c-d-e----
# ------e-d-e------
# --------e--------

# #size 10

# ------------------j------------------
# ----------------j-i-j----------------
# --------------j-i-h-i-j--------------
# ------------j-i-h-g-h-i-j------------
# ----------j-i-h-g-f-g-h-i-j----------
# --------j-i-h-g-f-e-f-g-h-i-j--------
# ------j-i-h-g-f-e-d-e-f-g-h-i-j------
# ----j-i-h-g-f-e-d-c-d-e-f-g-h-i-j----
# --j-i-h-g-f-e-d-c-b-c-d-e-f-g-h-i-j--
# j-i-h-g-f-e-d-c-b-a-b-c-d-e-f-g-h-i-j
# --j-i-h-g-f-e-d-c-b-c-d-e-f-g-h-i-j--
# ----j-i-h-g-f-e-d-c-d-e-f-g-h-i-j----
# ------j-i-h-g-f-e-d-e-f-g-h-i-j------
# --------j-i-h-g-f-e-f-g-h-i-j--------
# ----------j-i-h-g-f-g-h-i-j----------
# ------------j-i-h-g-h-i-j------------
# --------------j-i-h-i-j--------------
# ----------------j-i-j----------------
# ------------------j------------------

# The center of the rangoli has the first alphabet letter a, 
# and the boundary has the Nth alphabet letter (in alphabetical order).

# Function Description
# Complete the rangoli function in the editor below.
# rangoli has the following parameters:
# - int size: the size of the rangoli

# Returns
# - string: a single string made up of each of the lines of the rangoli 
# separated by a newline character (\n)

# Input Format
# Only one line of input containing , the size of the rangoli.

# Constraints
# 0 < size < 27

# Sample Input
# 5

# Sample Output
# --------e--------
# ------e-d-e------
# ----e-d-c-d-e----
# --e-d-c-b-c-d-e--
# e-d-c-b-a-b-c-d-e
# --e-d-c-b-c-d-e--
# ----e-d-c-d-e----
# ------e-d-e------
# --------e--------

# import the string module
import string

def print_rangoli(size):
    # your code goes here

    # create a variable that holds all the letters
    alpha = string.ascii_lowercase

    # TOP and BOTTOM PART

    # loop through the size in reverse order
    for i in range(size-1, 0, -1):

        # create a list that holds the size of the list
        row = ['-'] * (size*2-1)

        # loop through the size in reverse order
        for j in range(size-i):

            # set the value of the list to the letter for the top and bottom part
            row[size-1-j] = alpha[i+j]
            row[size-1+j] = alpha[i+j]

        # print the joined the rows
        print('-'.join(row))
    

    # MIDDLE

    # loop through the size
    for i in range(size):

        # create a list that holds the size of the list
        row = ['-'] * (size*2-1)

        # loop through the size
        for j in range(size-i):
            row[size-1-j] = alpha[i+j]
            row[size-1+j] = alpha[i+j]
        print('-'.join(row))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)