#
# @lc app=leetcode id=120 lang=python3
#
# [120] Triangle
#

# @lc code=start
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        dp = [[0]*n, [0]*n]
        for i in range(n):
            dp[(n-1)%2][i] = triangle[n-1][i]
        for i in range(n - 2, -1, -1):
            for j in range(i + 1):
                dp[i % 2][j] = min(dp[(i + 1) % 2][j], dp[(i + 1) % 2][j + 1]) + triangle[i][j]
        return dp[0][0]
        
# @lc code=end

