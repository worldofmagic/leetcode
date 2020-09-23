#
# @lc app=leetcode id=131 lang=python3
#
# [131] Palindrome Partitioning
#

# @lc code=start
from itertools import combinations

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        self.is_palindrome = lambda s : s == s[::-1]
        res = []
        self.helper(s, res, [])
        return res
    def helper(self, s, res, path):
        if not s:
            res.append(path)
            return res
        for i in range(1, len(s)+1):
            if self.is_palindrome(s[:i]):
                self.helper(s[i:], res, path + [s[:i]])

        
# @lc code=end

