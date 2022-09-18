#
# @lc app=leetcode id=228 lang=python3
#
# [228] Summary Ranges
#

# @lc code=start
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        l = len(nums)
        if l == 0:
            return []
        nums.append(float('inf'))
        res, start = [], 0
        for i in range(l):
            if nums[i + 1] != nums[i] + 1:
                res.append(str(nums[i]) if i == start else "%s->%s" % (nums[start], nums[i]))
                start = i + 1
        return res
    
        
# @lc code=end

