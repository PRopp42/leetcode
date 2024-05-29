"""
https://leetcode.com/problems/two-sum
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        A few things we can take advantage of:
            There is only one possible solution given any input.
            We also only need to return indexes, so duplicates i.e. 2 + 2 = 4 need to be accounted for
            but only if they're in the solution. We can discard them otherwise.
        """
        hashMap: dict[int, int] = {} # Hash map to store indices of previous numbers
        for i, x in enumerate(nums): # Iterate through the nums with index
            y = target - x
            if y in hashMap: # Have we seen the compliment yet?
                return[i, hashMap[y]] # If so, return it.

            hashMap[x] = i # Haven't seen the answer yet, might need it later.

        return [] # No dice. (We actually shouldn't hit this ever, given the constraints.)
    
"""
Analysis:
In a worst case, we need to examine every item in nums. O(n)
Insertion and access to a hashmap is O(1)
So, overall, we have an O(n)
"""