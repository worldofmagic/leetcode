#
# @lc app=leetcode id=107 lang=python3
#
# [107] Binary Tree Level Order Traversal II
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        # write your code here
        self.results = []
        if not root:
            return self.results
        q = [root]
        while q:
            next_level = []
            self.results.append([n.val for n in q])
            for node in q:
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            q = next_level
        return list(reversed(self.results))
        
# @lc code=end

