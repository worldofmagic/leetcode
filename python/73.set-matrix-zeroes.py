#
# @lc app=leetcode id=73 lang=python3
#
# [73] Set Matrix Zeroes
#

# @lc code=start
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = len(matrix)
        cols = len(matrix[0])
        zero_elements = []

        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    zero_elements.append([i,j])
        for element in zero_elements:
            for i in range(rows):
                matrix[i][element[1]] = 0
            for j in range(cols):
                matrix[element[0]][j] = 0
        
        
# @lc code=end

