#
# @lc app=leetcode id=463 lang=python3
#
# [463] Island Perimeter
#

# @lc code=start
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        perimeter = 0
        new_row = [0]*cols
        grid = [new_row] + grid + [new_row]
        grid = [[0]+row+[0] for row in grid]
        for i in range(rows+2):
            for j in range(cols+2):
                if grid[i][j] == 1:
                    perimeter += 1-grid[i-1][j]
                    perimeter += 1-grid[i+1][j]
                    perimeter += 1-grid[i][j-1]
                    perimeter += 1-grid[i][j+1]
        return perimeter
# @lc code=end

