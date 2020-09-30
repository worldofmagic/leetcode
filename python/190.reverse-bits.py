#
# @lc app=leetcode id=190 lang=python3
#
# [190] Reverse Bits
#

# @lc code=start
class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(32):
            print("res is {} and n is {}".format(bin(res), bin(n)))
            res = res << 1
            res += n & 1
            n = n >> 1
        return res
        
# @lc code=end

