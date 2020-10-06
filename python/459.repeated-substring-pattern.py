#
# @lc app=leetcode id=459 lang=python3
#
# [459] Repeated Substring Pattern
#

# @lc code=start
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)
        pattern = ""
        possible_pa = [i for i in range(1,n//2 + 1) if n%i == 0]
        for i in possible_pa:
            pattern = s[:i]
            count = n // i
            if pattern * count == s:
                return True
        return False

        
# @lc code=end

