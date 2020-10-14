#
# @lc app=leetcode id=128 lang=python3
#
# [128] Longest Consecutive Sequence
#

# @lc code=start
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        table = set(nums)
        max_length = 0
        for start in nums:
            if  start-1 not in table:
                end = start+1
                while end in table:
                    end += 1
                max_length = max(max_length, end-start)
        return max_length
        
# @lc code=end

