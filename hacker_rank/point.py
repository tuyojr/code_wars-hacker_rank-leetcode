# You are given four points A, B, C and D in a 3-dimensional Cartesian 
# coordinate system. You are required to print the angle between 
# the plane made by the points A, B, C and B, C, D in degrees(not radians). 
# Let the angle be PHI.
# Cos(PHI) = (X.Y)/|X||Y| where X = AB x BC and Y = BC x CD.

# Here, X.Y means the dot product of X and Y, and AB x BC means the cross
# product of vectors AB and BC. Also, AB = B - A.

# Input Format

# One line of input containing the space separated floating number values
# of the X, Y and Z coordinates of a point.

# Output Format

# Output the angle correct up to two decimal places.

# Sample Input

# 0 4 5
# 1 7 6
# 0 5 9
# 1 7 2

# Sample Output

# 8.19

import math

class Points(object):

    # create the __init__ method and set commands to be executed anytime
    # an object of this class is created
    def __init__(self, x, y, z):

        # set the x, y and z attributes of the object to the values
        self.x = x
        self.y = y
        self.z = z

    # create the __sub__ method and set commands to be executed anytime
    # the - operator is used on two objects of this class
    def __sub__(self, no):

        # subtract the x, y and z parts of the two points
        # and return the result
        return Points((self.x - no.x), (self.y - no.y), (self.z - no.z))

    # create a dot method and set commands to be executed at any time
    # the dot method is called on two objects of this class and adds the attributes
    def dot(self, no):

        # add the x, y and z parts of the two points
        # and return the result
        return (self.x * no.x + self.y * no.y + self.z * no.z)

    # create a cross method and set commands to be executed at any time
    # the cross method is called on two objects of this class and subtracts
    # a cross multiplication of the attributes on each other
    def cross(self, no):

        return Points((self.y * no.z - self.z * no.y), (self.z * no.x - self.x * no.z), (self.x * no.y - self.y * no.x))

    # create the absolute method and set commands to be executed at any time
    # the absolute method is called on the self and returns the power of the input
    def absolute(self):
        return pow((self.x ** 2 + self.y ** 2 + self.z ** 2), 0.5)

if __name__ == '__main__':
    points = list()
    for i in range(4):
        a = list(map(float, input().split()))
        points.append(a)

    a, b, c, d = Points(*points[0]), Points(*points[1]), Points(*points[2]), Points(*points[3])
    x = (b - a).cross(c - b)
    y = (c - b).cross(d - c)
    angle = math.acos(x.dot(y) / (x.absolute() * y.absolute()))

    print("%.2f" % math.degrees(angle))