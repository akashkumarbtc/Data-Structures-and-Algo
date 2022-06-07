"""
442. Find All Duplicates in an Array
Given an integer array nums of length n where all the integers of nums are in the range [1, n] and each integer appears once or twice, return an array of all the integers that appears twice.

You must write an algorithm that runs in O(n) time and uses only constant extra space.

 

Example 1:

Input: nums = [4,3,2,7,8,2,3,1]
Output: [2,3]
Example 2:

Input: nums = [1,1,2]
Output: [1]

"""

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        duplicate = {}
        
        if len(nums) == 0 or len(nums) == 1: return []
        
        for i in nums:
            if i in duplicate:
                duplicate[i] += 1
            else:
                duplicate[i] = 1

        return [k for k,v in duplicate.items() if duplicate[k] == 2]