#
# @lc app=leetcode.cn id=143 lang=python3
#
# [143] 重排链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        
        p = q = head
        while p.next:
            q = q.next
            p = p.next
            if p.next:
                p = p.next

        # 反转后边链表
        head2 = q
        t = s = q.next
        q.next = None
        while q != p:
            t = t.next
            s.next = q
            q, s = s, t
            
        # 插入回去
        t = head
        while t != head2 and q.next:
            s = q.next
            q.next = t.next
            t.next = q
            t = q.next
            q = s
        if q.next:
            t.next = q
        
# @lc code=end

