#
# @lc app=leetcode id=214 lang=python3
#
# [214] Shortest Palindrome
#

# @lc code=start
class Solution:
    def shortestPalindrome(self, s: str) -> str:
        if not s or s == "":
            return ""
        n = len(s)
        for i in range(n - 1, -1, -1):
            substr = s[:i + 1]
            if self.isPalindrome(substr):
                if i == n - 1:
                    return s 
                else:
                    return (s[i + 1:] [::-1]) + s[:]

    def isPalindrome(self, s):
        left, right = 0, len(s) - 1 
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1 
            right -= 1 
        
        return True
        
# @lc code=end
