#
# @lc app=leetcode id=342 lang=python3
#
# [342] Power of Four
#

# @lc code=start
class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        basic = 4
        i = 0
        while basic**i <= num:
            if basic**i == num:
                return True
            i += 1
        return False
# @lc code=end

