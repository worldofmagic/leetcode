#
# @lc app=leetcode id=162 lang=python3
#
# [162] Find Peak Element
#

# @lc code=start
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left, right = 0, len(nums)-1
        while left < right:
            mid1 = left + (right - left)//2
            mid2 = mid1+1
            if  nums[mid1] < nums[mid2]:
                left = mid2
            else:
                right = mid1
        return left

        
# @lc code=end

