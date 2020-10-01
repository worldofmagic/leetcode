#
# @lc app=leetcode id=257 lang=python3
#
# [257] Binary Tree Paths
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root:
            return []
        if root.left is None and root.right is None:
            return [str(root.val)]
        leftpath = self.binaryTreePaths(root.left)
        rightpath = self.binaryTreePaths(root.right)

        paths = []
        for path in leftpath + rightpath:
            paths.append(str(root.val)+'->'+path)
        return paths
        
# @lc code=end

