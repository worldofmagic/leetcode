#
# @lc app=leetcode id=98 lang=python3
#
# [98] Validate Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        res = []
        return self.inOrder(root, float('-inf'), float('inf'))
    
    def inOrder(self, root, min, max):
        if not root: return True
        if root.val >=max or root.val <= min: return False
        return self.inOrder(root.left, min, root.val) and self.inOrder(root.right,root.val, max)
        
# @lc code=end

