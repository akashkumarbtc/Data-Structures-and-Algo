"""
Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
Example 3:

Input: nums = [], target = 0
Output: [-1,-1]
"""

class Solution(object):
    def searchRange(self, nums, target):

        # Edge cases
        if len(nums) == 0: return [-1, -1]
        if len(nums) == 1: return ([0, 0] if nums[0] == target else [-1, -1])

        
        left = self.binarySearch(nums, target, True)    # Search for left most target
        right = self.binarySearch(nums, target, False)  # Search for right most target
        return [left, right]
    
    
    def binarySearch(self, nums, target, leftIndex ):
        
        start, end = 0, len(nums) - 1
        index = -1
        
        while start <= end:
            mid = ( start + end ) // 2
            
            if nums[mid] < target:
                start = mid + 1
            elif nums[mid] > target:
                end = mid - 1
            else:
                index = mid
                if leftIndex: end = mid - 1
                else: start = mid + 1
                    
        return index
                
            
        