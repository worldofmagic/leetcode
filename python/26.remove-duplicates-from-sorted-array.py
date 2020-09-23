#
# @lc app=leetcode id=26 lang=python3
#
# [26] Remove Duplicates from Sorted Array
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        flag = 0
        while flag < n-1:
            if nums[flag] == nums[flag + 1]:
                nums.pop(flag)
                n -= 1
            else:
                flag +=1
        return len(nums)
        
# @lc code=end

