#
# @lc app=leetcode id=28 lang=python3
#
# [28] Implement strStr()
#

# @lc code=start
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        if needle not in haystack:
            return -1
        if needle == haystack:
            return 0
        n = len(needle)
        m = len(haystack)
        if m <= n :
            return -1
        for i in range(m-n+1):
            if haystack[i: i+n] == needle:
                return i
        
        
# @lc code=end

