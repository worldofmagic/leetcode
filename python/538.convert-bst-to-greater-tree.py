#
# @lc app=leetcode id=538 lang=python3
#
# [538] Convert BST to Greater Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def convertBST(self, root: TreeNode) -> TreeNode:
        self.inorderTraversal(root, 0)
        return root
        



    def inorderTraversal(self, node: TreeNode, now_sum: int):
        if node is None: 
            return now_sum
        now_sum = self.inorderTraversal(node.right, now_sum)
        now_sum = now_sum + node.val
        node.val = now_sum
        now_sum = self.inorderTraversal(node.left, now_sum)
        return now_sum

        
# @lc code=end

