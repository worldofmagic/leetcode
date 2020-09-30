#
# @lc app=leetcode id=19 lang=python3
#
# [19] Remove Nth Node From End of List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        res = ListNode(0)
        res.next = head
        temp = res
        for i in range(n):
            head = head.next
        while head != None:
            head = head.next
            temp = temp.next
        temp.next = temp.next.next
        return res.next
        
# @lc code=end

