#
# @lc app=leetcode id=144 lang=python3
#
# [144] Binary Tree Preorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# class Solution:
#     def preorderTraversal(self, root: TreeNode) -> List[int]:
#         res = []
#         def dfs(cur):
#             if not cur: 
#                 return
#             res.append(cur.val)
#             dfs(cur.left)
#             dfs(cur.right)
#         dfs(root)
#         return res

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root: 
            return []
        pre_order = []
        stack = [root]
        while stack:
            top = stack.pop()
            pre_order.append(top.val)
            if top.right:
                stack.append(top.right)
            if top.left:
                stack.append(top.left)
        return pre_order
        
        
# @lc code=end

