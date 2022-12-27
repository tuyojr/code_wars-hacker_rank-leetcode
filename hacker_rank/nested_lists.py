# Given the names and grades for each student in a class of N students, 
# store them in a nested list and print the name(s) of any student(s) 
# having the second lowest grade.

# Note: If there are multiple students with the second lowest grade, 
# order their names alphabetically and print each name on a new line.

# Example
# records = [["chi", 20.0], ["beta", 50.0], ["alpha", 50.0]]

# The ordered list of scores is [20.0, 50.0], so the second lowest score is 50.0. 
# There are two students with that score: ["beta", "alpha"]. Ordered alphabetically, 
# the names are printed as:
# alpha
# beta

# Input Format
# The first line contains an integer, N, the number of students.
# The 2N subsequent lines describe each student over 2 lines.
# - The first line contains a student's name.
# - The second line contains their grade.

# Constraints
# 2 <= N <= 5
# There will always be one or more students having the second lowest grade.

# Output Format
# Print the name(s) of any student(s) having the second lowest grade in. 
# If there are multiple students, order their names alphabetically and 
# print each one on a new line.

# Sample Input 0
# 5
# Harry
# 37.21
# Berry
# 37.21
# Tina
# 37.2
# Akriti
# 41
# Harsh
# 39

# Sample Output 0
# Berry
# Harry

# Explanation 0
# There are  students in this class whose names and grades are assembled 
# to build the following list:

# python students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2],
#                      ['Akriti', 41], ['Harsh', 39]]

# The lowest grade of 37.2 belongs to Tina. The second lowest grade of 37.21
# belongs to both Harry and Berry, so we order their names alphabetically 
# and print each name on a new line.

if __name__ == '__main__':
    N = int(input())
    students = []

    for i in range(N):
        name = input()
        score = float(input())
        students.append([name, score])
    
    # reverse = None (Sorts in Ascending order)
    # key is set to sort using second element of 
    # sublist lambda has been used
    students.sort(key = lambda x: x[1])
    
    # list comprehension that removes the first lowest score from the original list
    # loops through each list in the students list and if the first score is not equal to the 
    # score of the second student, add it to this new list a
    a = [ i for i in students if i[1] != students[0][1]]

    # list comprehension to create a list of students with the same score.
    # this is created by looping through the initial list, a, above. if the
    # next student in the list has the same score as that in the previous student,
    # add it to this new list
    b = [ i for i in a if i[1] == a[0][1]]

    # this sorts the names in the nested list in an alphabetical order
    b.sort(key = lambda x: x[0])

    # loop through the length of final list and extract only the name 
    for i in range (len(b)):
        print(b[i][0])    