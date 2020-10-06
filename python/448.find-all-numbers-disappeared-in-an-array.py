#
# @lc app=leetcode id=448 lang=python3
#
# [448] Find All Numbers Disappeared in an Array
#

# @lc code=start
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # nums_set = set(nums)
        # res = [i for i in range(1, len(nums)+1) if i not in nums_set]
        # return res
        for i in nums:
            index = abs(i) -1
            nums[index] = 0-abs(nums[index])
        return [i+1 for i in range(len(nums)) if nums[i]>0]
# @lc code=end

