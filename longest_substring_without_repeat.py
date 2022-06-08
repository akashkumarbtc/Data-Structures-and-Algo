"""
3. Longest Substring Without Repeating Characters
Given a string s, find the length of the longest substring without repeating characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        if len(s) <= 1: return len(s)
        
        seen = {}
        max_len = 0
        start = 0
        for i in range(len(s)):
            if s[i] in seen:
                start = max(start, seen[s[i]] + 1)
            seen[s[i]] = i
            max_len = max(max_len, i - start + 1)
            
        return max_len