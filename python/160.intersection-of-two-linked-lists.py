#
# @lc app=leetcode id=160 lang=python3
#
# [160] Intersection of Two Linked Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        p1 = headA
        p2 = headB
        switch_count = 0
        while switch_count<=2:
            if p1 != p2:
                if p1 is not None and p2 is not None:
                    p1 = p1.next
                    p2 = p2.next
                elif p1 is None and p2 is not None:
                    p1 = headB
                    p2 = p2.next
                    switch_count += 1
                elif p2 is None and p1 is not None:
                    p2 = headA
                    p1 = p1.next
                    switch_count += 1
                else:
                    p1 = headB
                    p2 = headA
                    switch_count += 2
            else:
                return p1
        return None
        
# @lc code=end

