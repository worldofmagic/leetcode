#
# @lc app=leetcode id=102 lang=python3
#
# [102] Binary Tree Level Order Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        self.traverse(root, 0, res)
        return res
        

    def traverse(self, root, level, res):
        if not root: return
        if level >= len(res):
            res.append([])
        res[level].append(root.val)
        self.traverse(root.left, level + 1, res)
        self.traverse(root.right, level + 1, res)
        
# @lc code=end

