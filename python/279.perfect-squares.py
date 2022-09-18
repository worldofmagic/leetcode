#
# @lc app=leetcode id=279 lang=python3
#
# [279] Perfect Squares
#

# @lc code=start
class Solution:
    def numSquares(self, n: int) -> int:
        flag = n
        res = []
        while flag > 5:
            root = self.numSquares(flag)
            res.append(root)
            print(res)
            flag = n - root * root
        if flag == 5:
            res.append(2)
            return len(res)
        else:
            return 0

        
    
    def findRoot(self, n:int) -> int:
        for i in range(n, 0, -1):
            if i * i <= n:
                return i
        return 0
# @lc code=end

