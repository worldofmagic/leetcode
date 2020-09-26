#
# @lc app=leetcode id=45 lang=python3
#
# [45] Jump Game II
#

# @lc code=start
class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * n
        for i in range(1, n):
            dp[i] = float('inf')
            for j in range(i):
            	# 如果从j可以到跳到i
                if nums[j] + j >= i:
                    dp[i] = min(dp[i], dp[j] + 1)
        return dp[n - 1]
# @lc code=end

