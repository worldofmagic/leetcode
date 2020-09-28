#
# @lc app=leetcode id=118 lang=python3
#
# [118] Pascal's Triangle
#


# @lc code=start
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = [[1 for j in range(i)] for i in range(numRows+1)]
        for n in range(numRows+1):
            for m in range(n):
                if m>0 and m < n-1:
                    result[n][m] = result[n-1][m-1] + result[n-1][m]
        result.pop(0)
        return result
# @lc code=end

