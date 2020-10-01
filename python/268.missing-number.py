#
# @lc app=leetcode id=268 lang=python3
#
# [268] Missing Number
#

# @lc code=start
class Solution:
    # def missingNumber(self, nums: List[int]) -> int:
    #     if not nums:
    #         return []
    #     arr = sorted(nums)
    #     print(arr)
    #     for k,v in enumerate(arr):
    #         if k != v:
    #             return k
    #     return len(arr)
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        return n*(n+1)//2 - sum(nums)
        
# @lc code=end

