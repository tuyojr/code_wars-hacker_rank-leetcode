# Given an integer array nums, return true if any value appears at 
# least twice in the array, and return false if every element is distinct.

# Example 1:

# Input: nums = [1,2,3,1]
# Output: true

# Example 2:

# Input: nums = [1,2,3,4]
# Output: false

# Example 3:

# Input: nums = [1,1,1,3,3,4,3,2,4,2]
# Output: true

# Constraints:

# 1 <= nums.length <= 10^5
# -10^9 <= nums[i] <= 10^9

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        # create a dictionary to hold the elements and how many times they occur
        duplicate = {}

        # loop through the list of numbers
        for num in nums:

            # if the number is in the dictionary return True
            if num in duplicate:
                return True

            # otherwise add the number to the dictionary
            duplicate[num] = 1

        # if there are no duplicates at all, return false
        return False