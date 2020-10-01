#
# @lc app=leetcode id=389 lang=python3
#
# [389] Find the Difference
#

# @lc code=start
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        list_s = list(s)
        list_t = list(t)
        n = len(list_s)
        sum1 = 0
        for i in range(n):
            sum1 += ord(list_t[i]) - ord(list_s[i])
        sum1 += ord(list_t[-1])
        return chr(sum1)
        
# @lc code=end

