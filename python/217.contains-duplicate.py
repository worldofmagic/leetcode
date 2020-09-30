#
# @lc app=leetcode id=217 lang=python3
#
# [217] Contains Duplicate
#

# @lc code=start
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        set_nums = set()
        for i in nums:
            if i in set_nums:
                return True
            else:
                set_nums.add(i)
        return False
        
# @lc code=end

