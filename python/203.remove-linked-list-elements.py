#
# @lc app=leetcode id=203 lang=python3
#
# [203] Remove Linked List Elements
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if head is None:
            return head
        dummy = ListNode(0)
        dummy.next = head
        pre = dummy
        while head:
            if head.val == val:
                pre.next = head.next
                head = pre
            pre = head
            head = head.next
        return dummy.next
        
# @lc code=end

