#
# @lc app=leetcode id=202 lang=python3
#
# [202] Happy Number
#

# @lc code=start
class Solution:
    def isHappy(self, n: int) -> bool:
        d = {}
        while True:
            d[n] = 1
            n = sum([int(x)*int(x) for x in str(n)])
            if n == 1 or n in d:
                break
        return n == 1
        
# @lc code=end

