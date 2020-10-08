#
# @lc app=leetcode id=501 lang=python3
#
# [501] Find Mode in Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        self.freq = {}
        self.dfs(root)
        res = []
        max_freq = max(self.freq.values())
        print(self.freq)
        for k, v in self.freq.items():
            if v == max_freq:
                res.append(k)
        return res

    def dfs(self, node):
        if node is None:
            return
        self.dfs(node.left)
        self.dfs(node.right)

        if node.val in self.freq:
            self.freq[node.val] += 1
        else:
            self.freq[node.val] = 1
    
    # def findMode(self, root: TreeNode) -> List[int]:
    #     from collections import defaultdict
    #     if root == None:
    #         return []
    #     cache = defaultdict(int)
    #     self.helper(root, cache)
    #     max_freq = max(cache.values())
    #     result = [k for k,v in cache.items() if v == max_freq]
    #     return result

    # def helper(self, root, cache):
    #     if root == None:
    #         return
    #     cache[root.val] += 1
    #     self.helper(root.left, cache)
    #     self.helper(root.right, cache)
# @lc code=end

