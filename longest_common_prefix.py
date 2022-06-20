"""
14. Longest Common Prefix
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
"""

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        size = len(strs)
        if size == 0: return ""
        if size == 1: return strs[0]
        
        strs.sort()

        end = len(min(strs, key=len))
        
        i = 0
        
        while i < end and strs[0][i] == strs[size - 1][i]:
            i+= 1

        return strs[0][0: i]
            