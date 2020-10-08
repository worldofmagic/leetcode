#
# @lc app=leetcode id=492 lang=python3
#
# [492] Construct the Rectangle
#

# @lc code=start
class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        W, L = 1, area
        
        temp_min = float('inf')
        res = []
        while W <= L:
            if area % W == 0:
                L = area // W
                diff = abs(L-W)
                if diff < temp_min:
                    res = [L, W]
                    temp_min = diff
            W+=1
        return res

         
        
# @lc code=end

