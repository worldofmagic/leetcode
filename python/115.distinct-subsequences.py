#
# @lc app=leetcode id=115 lang=python3
#
# [115] Distinct Subsequences
#

# @lc code=start
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        # f[i][j] 表示S的前i个字符挑出t的前j个字符有多少种方法
        # 方案 sum()
        # 可行 or()
        # 最大 max()
        # 最小 min()
        dp = [[0 for j in range(len(t) + 1)] for i in range(len(s) + 1)]
        for i in range(len(s) + 1):
   		    dp[i][0] = 1
        for i in range(len(s)):
            for j in range(len(t)):
                if s[i] == t[j]:
                    dp[i+1][j+1] = dp[i][j+1] + dp[i][j]
                else:
                    dp[i+1][j+1] = dp[i][j + 1]
        return dp[len(s)][len(t)]
        
# @lc code=end

