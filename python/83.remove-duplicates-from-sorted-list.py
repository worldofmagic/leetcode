#
# @lc app=leetcode id=83 lang=python3
#
# [83] Remove Duplicates from Sorted List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return None
        p = head
        while p != None and p.next != None:
            if p.val != p.next.val:
                p = p.next
            elif p.val == p.next.val:
                p.next = p.next.next
        return head
# @lc code=end

