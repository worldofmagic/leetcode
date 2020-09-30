#
# @lc app=leetcode id=198 lang=python3
#
# [198] House Robber
#

# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        result = 0
        f, g, f1, g1 = 0, 0, 0, 0
        for x in nums:
            f1 = g + x
            g1 = max(f, g)
            g, f = g1, f1
       
        return max(f, g)

# @lc code=end

