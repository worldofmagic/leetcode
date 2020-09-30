#
# @lc app=leetcode id=171 lang=python3
#
# [171] Excel Sheet Column Number
#

# @lc code=start
class Solution:
    def titleToNumber(self, s: str) -> int:
        result = 0
        for i,n in enumerate(s[::-1]):
            result += (ord(n) -ord('A') + 1) * pow(26,i)
        return result
# @lc code=end

