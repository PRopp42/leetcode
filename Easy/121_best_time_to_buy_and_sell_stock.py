"""
https://leetcode.com/problems/best-time-to-buy-and-sell-stock
You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
"""

class Solution:
    """
    Dynamic Programming! We want to make sure we record the lowest value we've seen, and the highest profit against that.
    We get to take advantage of the fact that we can't buy stocks *after* we sell them. No reason to consider time travel.
    """
    def maxProfit(self, prices: List[int]) -> int:
        lowest: int = prices[0] # Initalizing to consider buying on the first day.
        profit: int = 0 # We need to have a floor of 0, so we don't return negative numbers.

        for val in prices:
            if val < lowest: # Is this a better day to buy?
                lowest = val
            if val - lowest > profit: # If we sold now, is this better than any other time?
                profit = val - lowest
        return profit
    
"""
Analysis:
We only need to consider each value in the price list once, so sticking with O(n)
(There is apparently a lot of linear time in the easy problems!)
"""