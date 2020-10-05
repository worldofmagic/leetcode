#
# @lc app=leetcode id=405 lang=python3
#
# [405] Convert a Number to Hexadecimal
#

# @lc code=start
class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return "0"
        ans = ""
        for i in range(8):
            n = num & 15
            if n > 9:
                n = chr(87+n)
            else:
                n = str(n)
            ans = n+ans
            num = num >> 4
        return ans.lstrip('0')
        
# @lc code=end

