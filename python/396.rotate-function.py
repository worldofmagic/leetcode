#
# @lc app=leetcode id=396 lang=python3
#
# [396] Rotate Function
#

# @lc code=start
class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        f = 0
        sum_nums = 0
        l = len(nums)
        for i, num in enumerate(nums):
            sum_nums += num
            f += i * num
        res = f
        for i in range(l-1, 0, -1):
            f = f + sum_nums - l*nums[i]
            res = max(res, f)
        return res

        
# @lc code=end

