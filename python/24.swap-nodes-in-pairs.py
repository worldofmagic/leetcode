#
# @lc app=leetcode id=24 lang=python3
#
# [24] Swap Nodes in Pairs
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        dummy = ListNode(0)
        dummy.next = head
        head = dummy
        while head.next and head.next.next:
            n1, n2 = head.next, head.next.next
            n1.next = n2.next
            n2.next = n1
            head.next = n2
            head = n1

        return dummy.next
        
# @lc code=end

