#
# @lc app=leetcode id=21 lang=python3
#
# [21] Merge Two Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
    #     head = ListNode(0)
    #     move = head
    #     if not l1:
    #         return l2
    #     if not l2:
    #         return l1
    #     while l1 and l2:
    #         if l1.val<l2.val:
    #             move.next = l1
    #             l1 = l1.next
    #         else:
    #             move.next = l2
    #             l2 = l2.next
    #         move = move.next
    #     if not l1:
    #         move.next = l2
    #     if not l2:
    #         move.next = l1
    #     return head.next
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(-1)
        p = dummy
        p1 = l1
        p2 = l2
        while p1 and p2:
            if p1.val < p2.val:
                p.next = p1
                p1 = p1.next
            else:
                p.next = p2
                p2 = p2.next
            p = p.next
        if p1:
            p.next = p1
        if p2:
            p.next = p2
        return dummy.next
                
# @lc code=end

