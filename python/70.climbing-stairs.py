#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0:
            return 1
        if n <= 2:
            return n
        a = 1
        b = 2
        for i in range(n-2):
            c   = a + b
            a = b
            b = c
        return b
        
# @lc code=end

