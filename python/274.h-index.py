#
# @lc app=leetcode id=274 lang=python3
#
# [274] H-Index
#

# @lc code=start
from queue import Empty


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        citations.sort()
        h = 0
        for i, c in enumerate(citations):
            h = max(h, min(n-i, c))
        return h
        
# @lc code=end

