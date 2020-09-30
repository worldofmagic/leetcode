#
# @lc app=leetcode id=169 lang=python3
#
# [169] Majority Element
#

# @lc code=start
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if not nums:
            return None
        temp_dict = {}
        for i in nums:
            if i not in temp_dict:
                temp_dict[i] = 1
            if temp_dict[i] > len(nums)//2:
                return i
            else:
                temp_dict[i] = temp_dict[i] + 1
        return None
# @lc code=end

