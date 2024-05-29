"""
https://leetcode.com/problems/valid-parentheses
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

  1  Open brackets must be closed by the same type of brackets.
  2  Open brackets must be closed in the correct order.
  3  Every close bracket has a corresponding open bracket of the same type.
"""
from collections import deque 
# We can just use lists, but deque is faster when using it as a stack

pairs = {')':'(', '}':'{', ']':'['}
# We want to know what characters close a pair

class Solution:
    def isValid(self, s: str) -> bool:
        """
        This is a perfect usecase for a first-in last-out (stack) data structure.
        We want to make sure that the latest parenthetical that was opened is the 
        next one we close.
        If we attempt to close to something out of order, we can just bail (return False)
        """
        stack = deque()
        for char in s:
            if char not in pairs:
                stack.append(char)
            else:
                if (len(stack) == 0) or (pairs[char] != stack.pop()):
                    return False

        return len(stack) == 0
    
"""
Analysis:
We have to check the entire string to ensure correctness, so that's O(n)
Stack interactions (append, pop) are O(1)
Overall, we're looking at O(n)
"""