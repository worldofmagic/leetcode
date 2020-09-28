#
# @lc app=leetcode id=110 lang=python3
#
# [110] Balanced Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        balanced, _ = self.validate(root)
        return balanced

    def validate(self, root):
        if root is None:
            return True, 0

        balanced, left_height = self.validate(root.left)
        if not balanced:
            return False, 0
        balanced, right_height = self.validate(root.right)
        if not balanced:
            return False, 0
        
        return abs(left_height - right_height)<=1, max(left_height, right_height) + 1

# @lc code=end

