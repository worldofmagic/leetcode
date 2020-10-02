#
# @lc app=leetcode id=392 lang=python3
#
# [392] Is Subsequence
#

# @lc code=start
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
        n = len(s)
        m = len(t)
        i,j = 0,0
        while i < n and j < m:
            if s[i] == t[j]:
                i += 1
            j+=1
        if i == n: 
            return True
        else:
            return False

        
# @lc code=end

