"""
https://leetcode.com/problems/valid-anagram
Given two strings s and t, return true if t is an anagram of s, and false otherwise.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
"""

from collections import Counter # hashmaps are wonderful

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        We want to make sure that each string has the same number of letters.
        We can use a basic counter and then, if the counts are equal, they are anagrams.
        """
        s_c = Counter(s)
        t_c = Counter(t)

        return s_c == t_c
    
"""
Analysis:
We need to traverse s & t once to count which is O(n)
Then compare the counter hashmaps (maximum of 26 keys) which should be O(1)
Overall, O(n)
"""