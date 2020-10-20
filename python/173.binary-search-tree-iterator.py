#
# @lc app=leetcode id=173 lang=python3
#
# [173] Binary Search Tree Iterator
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    # def __init__(self, root: TreeNode):
    #     self.root = root
    #     self.traverse = []
    #     self.in_order(root)

    # def in_order(self, node: TreeNode):
    #     if not node:
    #         return
    #     self.in_order(node.left)
    #     self.traverse.append(node.val)
    #     self.in_order(node.right)
        

    # def next(self) -> int:
    #     """
    #     @return the next smallest number
    #     """
    #     if self.traverse:
    #         return self.traverse.pop(0)
        

    # def hasNext(self) -> bool:
    #     """
    #     @return whether we have a next smallest number
    #     """
    #     return self.traverse != []

    def __init__(self, root: TreeNode):
        dummy = TreeNode(0)
        dummy.right = root
        self.stack = [dummy]
        self.next()

    def hasNext(self) -> bool:
        return bool(self.stack)
    
    def next(self) -> int:
        node = self.stack.pop()
        next_node = node
        if node.right:
            node = node.right
            while node:
                self.stack.append(node)
                node = node.left
        return next_node.val

        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
# @lc code=end

