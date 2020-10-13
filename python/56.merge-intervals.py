#
# @lc app=leetcode id=56 lang=python3
#
# [56] Merge Intervals
#

# @lc code=start
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key = lambda x:x[0])
        result = []
        for interval in intervals:
            print(result)
            if len(result) == 0 or result[-1][-1] < interval[0]:
                result.append(interval)
            else:
                result[-1][-1] = max(result[-1][-1], interval[-1])
        return result

        
# @lc code=end

