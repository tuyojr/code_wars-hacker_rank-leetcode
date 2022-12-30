# The provided code stub will read in a dictionary containing key/value 
# pairs of name:[marks] for a list of students. Print the average of the 
# marks array for the student name provided, showing 2 places after the 
# decimal.

# Example
# marks key:value pairs are
# 'alpha': [20, 30, 40]
# 'beta': [30, 50, 70]
# query_name = 'beta'

# The query_name is 'beta'. beta's average score is 
# (30 + 50 + 70)/3 = 50.0.

# Input Format

# The first line contains the integer n, the number of students' records. 
# The next n lines contain the names and marks obtained by a student, each 
# value separated by a space. The final line contains query_name, the 
# name of a student to query.

# Constraints
# 2 <= n <= 10
# 0 <= marks[i] <= 100
# length of marks arrays = 3

# Output Format
# Print one line: The average of the marks obtained by the particular 
# student correct to 2 decimal places.

# Sample Input 0
# 3
# Krishna 67 68 69
# Arjun 70 98 63
# Malika 52 56 60
# Malika

# Sample Output 0
# 56.00

# Explanation 0

# Marks for Malika are {52, 56, 60} whose average is (52 + 56 + 60) / 3 ==> 56 

# Sample Input 1
# 2
# Harsh 25 26.5 28
# Anurag 26 28 30
# Harsh

# Sample Output 1
# 26.50

if __name__ == '__main__':

    # take the user input for the total number of students
    n = int(input())

    # create an empty dictionary to hold each student name and their marks
    student_marks = {}

    # loop through the total number of students
    for _ in range(n):

        # each time the loop runs, allow the user input the name and score of
        # each student on the same line, separated by a space
        name, *line = input().split()

        # create a list of the students marks. they scores are mapped to each line
        scores = list(map(float, line))

        # update the dictionary with the student name as the key and list of scores as values
        student_marks[name] = scores
    
    # ask the user for the name of the student they wish to find the average of their scores
    query_name = input()

    # check if the name is in the student_marks dictionary
    if query_name in student_marks:

        # grab the requested student's name and store their list of scores in a variable
        values = student_marks.get(query_name)

        # calculate the total of their scores
        total = sum(values)

        # find the average of their scores
        average = total / len(values)

        # print the average to two decimal places (including zero), using the format method
        print(format(average, '.2f'))