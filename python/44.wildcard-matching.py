#
# @lc app=leetcode id=44 lang=python3
#
# [44] Wildcard Matching
#

# @lc code=start
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if s is None or p is None:
            return False
        n,m = len(s), len(p)

        dp = [[False]*(m+1) for _ in range(n+1)]

        dp[0][0] = True
        for i in range(1, m + 1):
            dp[0][i] = dp[0][i - 1] and p[i - 1] == '*'
        print(dp)
        
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if p[j - 1] == '*':
                    dp[i][j] = dp[i - 1][j] or dp[i][j - 1]
                else:
                    dp[i][j] = dp[i - 1][j - 1] and (s[i - 1] == p[j - 1] or p[j - 1] == '?')
        
        return dp[n][m]
# @lc code=end

