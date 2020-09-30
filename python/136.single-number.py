#
# @lc app=leetcode id=136 lang=python3
#
# [136] Single Number
#

# @lc code=start
class Solution:
    # def singleNumber(self, nums: List[int]) -> int:
    #     ans = 0
    #     for x in nums:
    #         ans = ans ^ x
    #     return ans
    
    def singleNumber(self, nums: List[int]) -> int:
        temp_dict = {}
        for i in nums:
            if i not in temp_dict:
                temp_dict[i] = 1
            else:
                temp_dict[i] = temp_dict[i] + 1
        result = {n:i for i,n in temp_dict.items()}
        return result[1]
        
# @lc code=end

