#
# @lc app=leetcode id=482 lang=python3
#
# [482] License Key Formatting
#

# @lc code=start
class Solution:
    def licenseKeyFormatting(self, S: str, K: int) -> str:
        char_arr = [char.upper() for char in S if char != '-']
        count = 0
        res = ""
        for c in char_arr[::-1]:
            if count == K:
                res = "-" + res
                count = 0
            res = c + res
            count += 1
        return res


        
# @lc code=end

