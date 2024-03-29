# collections.Counter()
# https://docs.python.org/3/library/collections.html#collections.Counter

# A counter is a container that stores elements as dictionary keys, and 
# their counts are stored as dictionary values.

# Sample Code

# >>> from collections import Counter
# >>> 
# >>> myList = [1,1,2,3,4,5,3,2,3,4,2,1,2,3]
# >>> print Counter(myList)
# Counter({2: 4, 3: 4, 1: 3, 4: 2, 5: 1})
# >>>
# >>> print Counter(myList).items()
# [(1, 3), (2, 4), (3, 4), (4, 2), (5, 1)]
# >>> 
# >>> print Counter(myList).keys()
# [1, 2, 3, 4, 5]
# >>> 
# >>> print Counter(myList).values()
# [3, 4, 4, 2, 1]
# Task

# Raghu is a shoe shop owner. His shop has X number of shoes.
# He has a list containing the size of each shoe he has in his shop.
# There are N number of customers who are willing to pay  amount of 
# money only if they get the shoe of their desired size.

# Your task is to compute how much money Raghu earned.

# Input Format

# The first line contains X, the number of shoes.
# The second line contains the space separated list of all the shoe sizes 
# in the shop.
# The third line contains N, the number of customers.
# The next N lines contain the space separated values of the shoe size 
# desired by the customer and x[i], the price of the shoe.

# Constraints
# 0 < X < 10^3
# 0 < N <= 10^3
# 20 < x[i] < 100
# 2 < shoe size < 20

# Output Format

# Print the amount of money earned by Raghu.

# Sample Input

# 10
# 2 3 4 5 6 8 7 6 5 18
# 6
# 6 55
# 6 45
# 6 55
# 4 40
# 18 60
# 10 50

# Sample Output

# 200

# Explanation

# Customer 1: Purchased size 6 shoe for $55.
# Customer 2: Purchased size 6 shoe for $45.
# Customer 3: Size 6 no longer available, so no purchase.
# Customer 4: Purchased size 4 shoe for $40.
# Customer 5: Purchased size 18 shoe for $60.
# Customer 6: Size 10 not available, so no purchase.

# Total money earned 55 + 45 + 40 + 60 = $200

from collections import Counter

if __name__ == "__main__":
    
    # create a variable for the total number of shoes
    X = int(input())
    
    # create a entry of all the available shoe sizes
    shoe_sizes = list(map(int, input().split()))
    
    # create a variable of the total number of customers
    N = int(input())
    
    # create a list of the customers shoe sizes and prices
    customers = []
    for i in range(N):
        customers.append(list(map(int, input().split())))

    # create a counter of the shoe sizes
    shoe_sizes_counter = Counter(shoe_sizes)
    
    # create a variable for the total amount of money earned
    total_amount = 0

    # iterate through the customers list
    for customer in customers:
    
        # if the customer's shoe size is in the shoe_sizes_counter
        if customer[0] in shoe_sizes_counter:

            # if the shoe size is available
            if shoe_sizes_counter[customer[0]] > 0:

                # add the price to the total money
                total_amount += customer[1]

                # subtract one from the shoe size counter
                shoe_sizes_counter[customer[0]] -= 1
            
    # print the total money earned
    print(total_amount)