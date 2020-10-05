#
# @lc app=leetcode id=434 lang=python3
#
# [434] Number of Segments in a String
#

# @lc code=start
class Solution:
    def countSegments(self, s: str) -> int:
        res = 0
        for i in range(len(s)):
            if s[i] != " " and (i==0 or s[i-1] ==" "):
                res += 1
        return res
        
# @lc code=end

