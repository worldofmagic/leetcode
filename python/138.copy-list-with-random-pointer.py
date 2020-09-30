#
# @lc app=leetcode id=138 lang=python3
#
# [138] Copy List with Random Pointer
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head: 
            return head
        # 复制影子节点
        p = head 
        while p: 
            add_node = Node(p.val)
            add_node.next = p.next 
            p.next = add_node
            p = p.next.next 
        # 复制随机指针
        p = head 
        while p: 
            if p.random: 
                p.next.random = p.random.next 
            p = p.next.next
        #　奇偶链表拆分
        p = head 
        dummy = Node(-1)
        copy_p = dummy
        while p: 
            copy_p.next = p.next 
            copy_p = copy_p.next 
            p.next = p.next.next
            p = p.next 
        return dummy.next 
        
# @lc code=end

