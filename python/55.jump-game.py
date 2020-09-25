#
# @lc app=leetcode id=55 lang=python3
#
# [55] Jump Game
#

# @lc code=start
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # f(i) = true 表达跳到了第i个位置
        # f(i) = OR(f(j), j<i && j 能跳到i)
        if not nums:
            return False
        n = len(nums)
        dp = [False]*n
        dp[0] = True

        for i in range(1,n):
            for j in range(i):
                if dp[j] and j+nums[j] >= i:
                    dp[i] = True
                    break
        return dp[n-1]

    def canJump(self, nums: List[int]) -> bool:
        n, rightmost = len(nums), 0
        for i in range(n):
            if i <= rightmost:
                rightmost = max(rightmost, i + A[i])
                if rightmost >= n - 1:
                    return True
        return False

        
# @lc code=end

