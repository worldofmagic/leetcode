#
# @lc app=leetcode id=25 lang=python3
#
# [25] Reverse Nodes in k-Group
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if head == None and head.next == None and k < 2:
            return head
        # 定义哨兵节点
        dummy = ListNode(0)
        # 指向节点
        dummy.next = head

        # 定义前驱后继节点
        pre = dummy
        tail = dummy

        # 控制 tail 到待翻转链表部分的末尾
        while True:
            count = k
            while count > 0 and tail != None:
                count -= 1
                tail = tail.next
            # 到达尾部时，长度不足 k 时，跳出循环
            if tail == None:
                break

            # 这里用于下次循环
            head = pre.next
            # 开始进行翻转
            while pre.next != tail:
                tmp = pre.next
                pre.next = tmp.next
                tmp.next = tail.next
                tail.next = tmp
            
            # 重置指针
            pre = head
            tail = head
        
        return dummy.next
       
# @lc code=end

