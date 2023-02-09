# You are given an array prices where prices[i] is the price of a 
# given stock on the ith day.

# You want to maximize your profit by choosing a single day to buy 
# one stock and choosing a different day in the future to sell that stock.

# Return the maximum profit you can achieve from this transaction. 
# If you cannot achieve any profit, return 0.

# Example 1:

# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), 
# profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because 
# you must buy before you sell.

# Example 2:

# Input: prices = [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transactions are done and the max profit = 0.

# Constraints:

# 1 <= prices.length <= 10^5
# 0 <= prices[i] <= 10^4

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        # initialize the max profit
        max_profit = 0

        # initialize the min price
        min_price = float("inf")

        # loop through the list
        for price in prices:

            # if the price is less than the min price
            if price < min_price:

                # set the min price to the price
                min_price = price

            # otherwise if the price minus the min price is greater than the max profit
            elif price - min_price > max_profit:

                # set the max profit to the price minus the min price
                max_profit = price - min_price

        # return the max profit
        return max_profit