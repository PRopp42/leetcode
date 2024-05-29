"""
https://leetcode.com/problems/valid-palindrome/
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.
Given a string s, return true if it is a palindrome, or false otherwise.
"""

import string # I really don't want to ennumerate all punctuation. #lazyengineer

class Solution:
    """
    We need to clean up the string and then make sure the opposite index matches.
    """
    def isPalindrome(self, s: str) -> bool:
        # Clean the string
        s = s.lower()
        s = "".join([x for x in s if x not in string.punctuation+" "]) # List comprehension is fast but terrible for readability.

        for i, x in enumerate(s):
            if i > (len(s) /2): # If we hit the halfway point, we're done!
                return True
            if x != s[-(1+i)]: # If we find that the other character doesn't match, we're also done.
                return False
        return True # Sometimes you get an empty string. Which is technically a palindrome.
    
"""
Analysis:
Worst case, we need to traverse the string 1.5 times (technically 2.5 times, since we clean in two steps), so we're in the O(n) family
"""