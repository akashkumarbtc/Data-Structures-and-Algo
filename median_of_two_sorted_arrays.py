"""
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

 

Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
"""

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """
        :type nums1: List[int] => A
        :type nums2: List[int] => B
        :rtype: float
        """
        # to make sure nums1 is always the one with shorter length
        if len(nums1) > len(nums2) :
            return self.findMedianSortedArrays(nums2, nums1)
        
        total_len = len(nums1) + len(nums2)
        half = total_len // 2
        
        left, right = 0, len(nums1) - 1
        while True:
            midA = (left + right) // 2
            midB = half - midA - 2
            
            Aleft = nums1[midA] if midA >= 0 else float("-infinity")
            Aright = nums1[midA + 1] if (midA + 1) < len(nums1) else float("infinity")
            
            Bleft = nums2[midB] if midB >= 0 else float("-infinity")
            Bright = nums2[midB + 1]  if (midB + 1) < len(nums2) else float("infinity")
            
            # partition is correct
            if Aleft <= Bright and Bleft <= Aright:
                # if total length is odd - only one mid value exists
                if total_len % 2:
                    print("here")
                    return min(Aright, Bright)
                
                # if total length is even - median is avg of middle 2 elements
                return ((max(Aleft, Bleft) + min(Aright, Bright)) / 2)
            elif Aleft > Bright:
                right = midA - 1
            else:
                left = midA + 1