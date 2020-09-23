#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#

# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        n = len(nums)
        max_sum = nums[0]
        for i in range(n):
            for j in range(i+1, n+1):
                if max_sum is None or max_sum < sum(nums[i:j]):
                    max_sum = sum(nums[i:j])
        return max_sum

        
# @lc code=end

