#
# @lc app=leetcode id=33 lang=python3
#
# [33] Search in Rotated Sorted Array
#

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        start, end = 0, len(nums)-1
        while start+1 < end:
            mid = start + (end - start)//2
            if nums[start]<= nums[mid]:
                if nums[start]<=target <=nums[mid]:
                    end = mid
                else:
                    start = mid
            else:
                if nums[mid] <= target <=nums[end]:
                    start = mid
                else:
                    end = mid
        if nums[start] == target:
            return start
        if nums[end] == target:
            return end
        return -1

# @lc code=end

