#
# @lc app=leetcode id=57 lang=python3
#
# [57] Insert Interval
#

# @lc code=start
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = intervals
        res.append(newInterval)
        print(res)
        return self.merge(res)
        
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

