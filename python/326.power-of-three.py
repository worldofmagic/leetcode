#
# @lc app=leetcode id=326 lang=python3
#
# [326] Power of Three
#

# @lc code=start
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        basic = 3
        i = 0
        while basic**i <= n:
            if basic**i == n:
                return True

            i += 1
        return False

        
# @lc code=end

