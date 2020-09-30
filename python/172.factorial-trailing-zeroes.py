#
# @lc app=leetcode id=172 lang=python3
#
# [172] Factorial Trailing Zeroes
#

# @lc code=start
class Solution:
    def trailingZeroes(self, n: int) -> int:
        if n >= 5:
            return n//5 + self.trailingZeroes(n//5)
        else:
            return 0
        
# @lc code=end

