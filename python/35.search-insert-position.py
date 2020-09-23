#
# @lc app=leetcode id=35 lang=python3
#
# [35] Search Insert Position
#

# @lc code=start
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n = len(nums)
        left, right = 0, n-1
        if nums[0] > target:
            return 0

        while left+1 < right:
            mid =left+(right-left)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid
            else:
                right = mid
        if nums[right] == target:
            return right
        if nums[right] < target:
            return right+1
        if nums[left] == target:
            return left
        return left+1
        
# @lc code=end

