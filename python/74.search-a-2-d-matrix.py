#
# @lc app=leetcode id=74 lang=python3
#
# [74] Search a 2D Matrix
#

# @lc code=start
class Solution:
    # def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
    #     col = len(matrix[0])
    #     left, right = 0, len(matrix) * col - 1
    #     while left < right:
    #         mid = (right + left) // 2
    #         value = matrix[mid // col][mid % col]
    #         if value == target:
    #             return True
    #         elif value > target:
    #             right = mid
    #         else:
    #             left = mid + 1
    #     if matrix[right // col][right % col] == target:
    #         return True
    #     return False
    
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        row = len(matrix)
        col = len(matrix[0])
        i = 0
        j = col-1
        while i < row and j >= 0:
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] < target:
                i += 1
            elif matrix[i][j] > target:
                j -= 1
        return False
        
# @lc code=end

