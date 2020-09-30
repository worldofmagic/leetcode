#
# @lc app=leetcode id=32 lang=python3
#
# [32] Longest Valid Parentheses
#

# @lc code=start
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if not s:
            return 0
        
        n = len(s)
        dp = [ 0 for _ in range(n)]
        res = 0
        for i in range(len(s)-2, -1, -1):
            if s[i] == "(":
                j = i + dp[i+1]+1
                if j < len(s) and s[j] == ")":
                    dp[i] = dp[i+1]+2
                    if j+1 < len(s):
                        dp[i] += dp[j+1]
                res = max(res, dp[i])
        return res

        
# @lc code=end

