#
# @lc app=leetcode id=27 lang=python3
#
# [27] Remove Element
#

# @lc code=start
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        flag = 0
        while flag < n:
            if nums[flag] == val:
                nums.pop(flag)
                n -= 1
            else:
                flag+=1
        return len(nums)
        
# @lc code=end

