#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""

        n = len(s)
        is_palindrome = [[False]*n for _ in range(n)]

        for i in range(n):
            is_palindrome[i][i] = True
        for i in range(1,n):
            is_palindrome[i][i-1] = True
        
        longest, start, end = 1, 0, 0
        for length in range(1,n):
            for i in range(n-length):
                j = i + length
                is_palindrome[i][j] = s[i] == s[j] and is_palindrome[i+1][j-1]
                if is_palindrome[i][j] and length+1 > longest:
                    longest = length + 1
                    start, end = i, j
        return s[start: end+1]
            
# @lc code=end

