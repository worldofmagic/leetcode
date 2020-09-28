#
# @lc app=leetcode id=119 lang=python3
#
# [119] Pascal's Triangle II
#

# @lc code=start
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        numRows = rowIndex+2
        result = [[1 for j in range(i)] for i in range(numRows)]
        for n in range(numRows):
            for m in range(n):
                if m>0 and m < n-1:
                    result[n][m] = result[n-1][m-1] + result[n-1][m]
        result.pop(0)
        return result[rowIndex]
        
# @lc code=end

