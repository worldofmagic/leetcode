#
# @lc app=leetcode id=409 lang=python3
#
# [409] Longest Palindrome
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> int:
        extra = {}

        for c in s:
            if c in extra:
                del extra[c]
            else:
                extra[c] = True

        remove = len(extra)
        if remove > 0:
            remove -= 1
    
        return len(s) - remove

        
        
# @lc code=end

