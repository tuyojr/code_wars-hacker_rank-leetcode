# Take an array and remove every second element from the array. 
# Always keep the first element and start removing with the next element.

# Example:
# ["Keep", "Remove", "Keep", "Remove", "Keep", ...] --> ["Keep", "Keep", "Keep", ...]

# None of the arrays will be empty, so you don't have to worry about that!

def remove_every_other(my_list):
    # Your code here!
    
    # create a list to hold the elements that meet the criteria
    new_list = []

    # loop through the list
    for i in range(len(my_list)):
        # if the index is even, add the element to the new list
        if i % 2 == 0:
            new_list.append(my_list[i])
        
    return new_list

    # # one line solution
    # return my_list[::2]

# test.assert_equals(remove_every_other(['Hello', 'Goodbye', 'Hello Again']),
#                    ['Hello', 'Hello Again'])
# test.assert_equals(remove_every_other([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]),
#                    [1, 3, 5, 7, 9])
# test.assert_equals(remove_every_other([[1, 2]]), [[1, 2]])
# test.assert_equals(remove_every_other([['Goodbye'], {'Great': 'Job'}]),
#                    [['Goodbye']])