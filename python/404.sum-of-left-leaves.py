#
# @lc app=leetcode id=404 lang=python3
#
# [404] Sum of Left Leaves
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        return self.dfs(root)

    def dfs(self, root):
        if not root:
            return 0
        res = 0
        if root.left:
            left = root.left
            #当前节点的左儿子,并判断是否为叶子节点
            if not left.left and not left.right:
                res += left.val
            else :
                res += self.dfs(left)
        if root.right:
            right = root.right
            res += self.dfs(right)
        return res
        
# @lc code=end

