#
# @lc app=leetcode id=168 lang=python3
#
# [168] Excel Sheet Column Title
#

# @lc code=start
class Solution:
    def convertToTitle(self, n: int) -> str:
        result = ''
        while n > 0:
            if n % 26 == 0:
                result += chr(ord('Z'))
                n -= 26
            else:
                result += chr(ord('A') + n % 26 - 1)
            n //= 26
        return result[::-1]

        
# @lc code=end

