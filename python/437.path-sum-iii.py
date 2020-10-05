#
# @lc app=leetcode id=437 lang=python3
#
# [437] Path Sum III
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def DFS(self, root, su, tmp):
        if None==root:
            return 0
        else:
            flag=0
            if su==tmp+root.val:
                flag=1
            return flag+self.DFS(root.left, su, tmp+root.val)+self.DFS(root.right, su, tmp+root.val)
    
    def pathSum(self, root: TreeNode, sum: int) -> int:
        #write your code here
        if None==root:
            return 0
        else:
            return self.DFS(root, sum, 0)+self.pathSum(root.left, sum)+self.pathSum(root.right, sum)


    
            
        

# @lc code=end

