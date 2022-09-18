#
# @lc app=leetcode id=199 lang=python3
#
# [199] Binary Tree Right Side View
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if not root: return []
        self.view(root, 0, res)
        return [i[-1] for i in res]

    def view(self, root, level, res):
        if not root: return
        if level >= len(res):
            res.append([])
        res[level].append(root.val)
        self.view(root.left, level+1, res)
        self.view(root.right, level+1, res)
        
# @lc code=end

