#
# @lc app=leetcode id=215 lang=python3
#
# [215] Kth Largest Element in an Array
#

import heapq

# @lc code=start
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return sorted(nums,reverse=True)[k-1]
        # return heapq.nlargest(k,nums)[-1]
# @lc code=end

