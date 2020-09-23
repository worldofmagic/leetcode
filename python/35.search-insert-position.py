#
# @lc app=leetcode id=35 lang=python3
#
# [35] Search Insert Position
#

# @lc code=start
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        start, end = 0, len(nums)-1
        while start+1 < end:
            mid = start + (end-start)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                start = mid
            else:
                end = mid
        if target<= nums[start]:
            return start
        if target> nums[end]:
            return end+1
        return end
        

        
# @lc code=end

