#
# @lc app=leetcode id=141 lang=python3
#
# [141] Linked List Cycle
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if head is None:			
            return False		
        p1 = head		
        p2 = head		
        while True:
            if p1.next is not None:
                p1=p1.next.next
                p2=p2.next
                if p1 is None or p2 is None:
                    return False
                elif p1 == p2:
                    return True
            else:
                return False
        return False



            
# @lc code=end

