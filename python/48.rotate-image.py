#
# @lc app=leetcode id=48 lang=python3
#
# [48] Rotate Image
#

# @lc code=start
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = len(matrix)
        cols = len(matrix[0])
        for i in range(rows//2):
            for j in range(cols):
                matrix[i][j], matrix[rows-i-1][j] = matrix[rows-i-1][j], matrix[i][j]
        for i in range(rows):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        
# @lc code=end

