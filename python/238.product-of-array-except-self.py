#
# @lc app=leetcode id=238 lang=python3
#
# [238] Product of Array Except Self
#

# @lc code=start
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        prod = 1
        l = len(nums)
        for i in range(l):
            res.append(prod)
            prod *= nums[i]
        prod = 1
        for i in range(l - 1, -1 , -1):
            res[i] *= prod
            prod *= nums[i]
        return res
        
            
# @lc code=end

