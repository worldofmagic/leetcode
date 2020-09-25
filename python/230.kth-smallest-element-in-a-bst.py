#
# @lc app=leetcode id=230 lang=python3
#
# [230] Kth Smallest Element in a BST
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        self.k = k
        self.result = None
        self.helper(root)
        return self.result

    
    def helper(self,node: TreeNode):
        if node is None:
            return
        self.helper(node.left)
        self.k -= 1
        if self.k == 0:
            self.result = node.val
        if self.k > 0:
            self.helper(node.right)

        
# @lc code=end

