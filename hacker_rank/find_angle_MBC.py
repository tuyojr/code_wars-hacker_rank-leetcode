# # Image link
# # https://s3.amazonaws.com/hr-challenge-images/9668/1440151155-10b2b748ee-rsz_1438840048-2cf71ed69d-findangle.png

# ABC is a right triangle, 90° at B.
# Therefore, angleABC = 90°.

# Point M is the midpoint of hypotenuse AC.

# You are given the lengths AB and BC.
# Your task is to find angleMBC (angle theta°, as shown in the figure) in degrees.

# Input Format

# The first line contains the length of side AB.
# The second line contains the length of side BC.

# Constraints
# - 0 < AB <= 100
# - 0 < BC <= 100
# - Lengths AB and BC are natural numbers.

# Output Format

# Output angleMBC in degrees.

# Note: Round the angle to the nearest integer.

# Examples:
# If angle is 56.5000001°, then output 57°.
# If angle is 56.5000000°, then output 57°.
# If angle is 56.4999999°, then output 56°.
# 0° < theta° < 90°

# Sample Input

# 10
# 10

# Sample Output

# 45°

import math

if __name__ == '__main__':
    AB = int(input())
    BC = int(input())

    # Calculate the hypotenuse
    AC = math.sqrt(AB**2 + BC**2)

    # Calculate the angle
    angleMBC = round(math.degrees(math.acos(BC/AC)))

    # Print the angle
    print(str(angleMBC) + "°") # print(str(angleMBC) + chr(176))