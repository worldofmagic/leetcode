#
# @lc app=leetcode id=263 lang=python3
#
# [263] Ugly Number
#

# @lc code=start
class Solution:
    def isUgly(self, num: int) -> bool:
        if num <= 0:
            return False
        if num == 1:
            return True
        while num >= 5 and num%5 ==0:
            num = num//5
        while num >= 3 and num%3 ==0:
            num = num//3
        while num >= 2 and num%2 ==0:
            num = num//2
        return num == 1
        
# @lc code=end

