# Mr. Anant Asankhya is the manager at the INFINITE hotel. 
# The hotel has an infinite amount of rooms.

# One fine day, a finite number of tourists come to stay at the hotel.
# The tourists consist of:
# → A Captain.
# → An unknown group of families consisting of K members per group where K ≠ 1.

# The Captain was given a separate room, and the rest were given one room per group.

# Mr. Anant has an unordered list of randomly arranged room entries. 
# The list consists of the room numbers for all of the tourists. 
# The room numbers will appear K times per group except for the Captain's room.

# Mr. Anant needs you to help him find the Captain's room number.
# The total number of tourists or the total number of groups of families is 
# not known to you.
# You only know the value of K and the room number list.

# Input Format

# The first line consists of an integer, K, the size of each group.
# The second line contains the unordered elements of the room number list.

# Constraints
# 1 < K < 1000

# Output Format

# Output the Captain's room number.

# Sample Input

# 5
# 1 2 3 6 5 4 4 2 5 3 6 1 6 5 3 2 4 1 2 5 1 4 3 6 8 4 3 1 5 6 2

# Sample Output

# 8

# Explanation

# The list of room numbers contains 31 elements. Since K is 5, there must 
# be 6 groups of families.
# In the given list, all of the numbers repeat 5 times except for room number 8.
# Hence, 8 is the Captain's room number.

# Enter your code here. Read input from STDIN. Print output to STDOUT

if __name__ == '__main__':
    # create a variable to store the size of each group
    K = int(input())
    
    # create a list for the room numbers
    unordered_room_numbers = list(map(int, input().split()))

    # create a dictionary to hold all the room numbers of group members
    d = dict()

    # loop through the unordered room numbers and update the dictionary
    # with the number of times they appear
    for room in unordered_room_numbers:
        d[room] = d.get(room, 0) + 1

    # loop through the dictionary to get a key that has a value of 1
    # this will be the captain's room
    for key, value in d.items():
        if value == 1:
            print(key)

# if __name__ == '__main__':

#     # create a variable to store the size of each group
#     K = int(input())
    
#     # create a list for the room numbers
#     unordered_room_numbers = list(map(int, input().split()))

#     # create a set to hold all the room numbers of group members
#     s = set()

#     # loop through the unordered room numbers and update the set
#     # with the number of times they appear
#     for room in unordered_room_numbers:
#         if room in s:
#             s.remove(room)
#         else:
#             s.add(room)

#     # print the captain's room
#     print(s.pop())