#
# @lc app=leetcode id=191 lang=python3
#
# [191] Number of 1 Bits
#

# @lc code=start
class Solution:
    def hammingWeight(self, n: int) -> int:
        # write your code here
        ones = 0
        while n != 0:
            ones += (n & 1)
            n = n >> 1
        return ones
# @lc code=end

