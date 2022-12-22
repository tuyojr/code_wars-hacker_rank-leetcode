# There is a horizontal row of n cubes. The length of each cube is given. 
# You need to create a new vertical pile of cubes. The new pile should 
# follow these directions: if cube[i] is on top of cube[j] then 
# sideLength[j] >= sideLength[i].
# When stacking the cubes, you can only pick up either the leftmost or the 
# rightmost cube each time. Print Yes if it is possible to stack the cubes. 
# Otherwise, print No.

# Example

# blocks = [1,2,3,8,7]
# Result: No
# After choosing the rightmost element, 7, choose the leftmost element, 1. 
# After than, the choices are 2 and 8. These are both larger than the top 
# block of size 1.

# blocks = [1,2,3,7,8]
# Result: Yes
# Choose blocks from right to left in order to successfully stack the blocks.

# Input Format
# The first line contains a single integer T, the number of test cases.
# For each test case, there are 2 lines.
# The first line of each test case contains n, the number of cubes.
# The second line contains n space separated integers, denoting the 
# sideLengths of each cube in that order.

# Constraints
# 1 <= T <= 5
# 1 <= n <= 10^5
# 1 <= sideLength < 2^31

# Output Format
# For each test case, output a single line containing either Yes or No.

# Sample Input
# STDIN        Function
# -----        --------
# 2            T = 2
# 6            blocks[] size n = 6
# 4 3 2 1 3 4  blocks = [4, 3, 2, 1, 3, 4]
# 3            blocks[] size n = 3
# 1 3 2        blocks = [1, 3, 2]

# Sample Output
# Yes
# No

# Explanation

# In the first test case, pick in this order: left - 4, right - 4, left - 3, 
# right - 3, left - 2, right - 1.
# In the second test case, no order gives an appropriate arrangement of 
# vertical cubes. 3 will always come after either 1 or 2.

# Enter your code here. Read input from STDIN. Print output to STDOUT

# define a function that checks if a cube can be piled or not
# it will travel through the user's list from left and right to check if
# they can be piled up depending o which value is greater.
def piler(side_length):
    
    # define a variable that checks the left index
    left_index = 0
    
    # define a variable that checks the value right of the index
    right_index = len(side_length) - 1
    
    # since we don't know the current length of the cube, we define a variable that is infinity.
    # this length will be updated when we know the current length after comparing the left and right values
    current_cube_length = float("inf")
    
    # use a wile loop to travel across the list and check when the left_index
    # is less than or equal to the right_index, we want to break out of the condition
    while left_index <= right_index:
        
        # since we are not comparing the index, create a variable to hold the values
        # at the left and right indexes of the list
        left_value = side_length[left_index]
        right_value = side_length[right_index]
    
        # now lets check if we can pile them on each other or not
        if left_value >= right_value and left_value <= current_cube_length:
            
            # update the cube length
            current_cube_length = left_value
            
            # increment the index form the left to go to the next value
            left_index += 1
        elif right_value >= left_value and right_value <= current_cube_length:
            
            # update the cube length
            current_cube_length = right_value
            
            # decrement the index from the right to go to the next value
            right_index -= 1
        else:
            
            # if we're unable to pile it
            return "No"
        
    # if we're able to pile it
    return "Yes"

# create a variable for the test cases ---> T
T = int(input())

# loop through each test case.
for test_case in range(T):
    # prompt the user for the number of values in each horizontal cube
    n = int(input())
    
    # prompt the user to enter the list of values in each horizontal cube
    # this list will be updated each time a value is entered
    side_length = [int(length) for length in input().split()]
    
    print(piler(side_length))
    
    