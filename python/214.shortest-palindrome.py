#
# @lc app=leetcode id=214 lang=python3
#
# [214] Shortest Palindrome
#

# @lc code=start
import collections
class Solution:
    def shortestPalindrome(self, s: str) -> str:
        """
        :type s: str
        :rtype: str
        """
        N = len(s)
        if N == 0: return ""
        t = s[::-1]
        for i in range(N, 0, -1):
            if s[:i] == t[N - i:]:
                break
        return t[:N - i] + s
        
# @lc code=end
