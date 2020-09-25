#
# @lc app=leetcode id=67 lang=python3
#
# [67] Add Binary
#

# @lc code=start
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        indexa = len(a) - 1
        indexb = len(b) - 1
        carry = 0
        addsum = ""
        while indexa >= 0 or indexb >= 0:
            x = int(a[indexa]) if indexa >= 0 else 0
            y = int(b[indexb]) if indexb >= 0 else 0
            if (x + y + carry) % 2 == 0:
                addsum = '0' + addsum
            else:
                addsum = '1' + addsum
            carry = (x + y + carry) // 2
            indexa, indexb = indexa - 1, indexb - 1
        if carry == 1:
            addsum = '1' + addsum
        return addsum


        
# @lc code=end

