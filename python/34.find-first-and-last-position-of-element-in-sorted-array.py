#
# @lc app=leetcode id=34 lang=python3
#
# [34] Find First and Last Position of Element in Sorted Array
#

# @lc code=start
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        if nums[0] > target or nums[-1] < target:
            return [-1, -1]
        start, end = 0, len(nums) - 1
        res = []

        # find left
        while start+1 < end:
            mid = (start + end )//2
            if nums[mid] >= target:
                end = mid
            else:
                start = mid
        if nums[start] == target:
            res.append(start)
        elif nums[end] == target:
            res.append(end)
        else:
            return [-1,-1]

        # find right
        start, end = 0, len(nums) - 1
        while start+1 < end:
            mid = (start + end )//2
            if nums[mid] <= target:
                start = mid
            else:
                end = mid
        if nums[end] == target:
            res.append(end)
        elif nums[start] == target:
            res.append(start)
        return res


        
# @lc code=end

