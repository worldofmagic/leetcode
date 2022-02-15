#
# @lc app=leetcode id=145 lang=python3
#
# [145] Binary Tree Postorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            dfs(node.right)
            res.append(node.val)
        dfs(root)
        return res
            


# class Solution:
#     def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
#         if not root:
#             return []
        
#         result , stack = [], []
#         prev, node = None, root
        
#         while stack or node:
#             # if node is valid, add it to the stack and keep going left
#             if node:
#                 stack.append(node)
#                 node = node.left
#             else:
#                 # done with all left children for this node
#                 top = stack[-1]
                
#                 # check if this top of stack node has any right children yet to be explored
#                 # Also, make sure that right child wasn't just previously visited
#                 if top.right and top.right != prev:
#                     node = top.right
#                 else:
#                     # no right child, so this should be a leaf node
#                     result.append(top.val)
#                     prev = top
#                     stack.pop()
        
#         return result
        
# @lc code=end

