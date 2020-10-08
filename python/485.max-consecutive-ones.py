#
# @lc app=leetcode id=485 lang=python3
#
# [485] Max Consecutive Ones
#

# @lc code=start
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = -float("inf")
        count = 0
        n = len(nums)
        for i in range(n):
            if nums[i] == 1:
                count += 1
            elif nums[i] == 0:
                res = max(res, count)
                count = 0
        res = max(res,count)
        return res
        
# @lc code=end

