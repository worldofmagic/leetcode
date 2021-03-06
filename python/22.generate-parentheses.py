#
# @lc app=leetcode id=22 lang=python3
#
# [22] Generate Parentheses
#

# @lc code=start
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n ==0:
            return []
        res = []
        self.backtrack(n,n,"",res)
        return  res

    def backtrack(self, l, r, item, res):
        if  r<l:
            return
        if l==0 and r==0:
            res.append(item)
        if l>0:
            self.backtrack(l-1,r,item+"(",res)
        if r>0:
            self.backtrack(l,r-1,item+")",res)
# @lc code=end

