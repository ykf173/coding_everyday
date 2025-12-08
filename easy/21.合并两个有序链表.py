#
# @lc app=leetcode.cn id=21 lang=python3
#
# [21] 合并两个有序链表
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional
class Solution:
     def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        p = ListNode(-1000, list1)
        q, t = list2, list1
        list1 = p
        while t and q:
            while t and q and t.val >= q.val:
                p.next = q
                q = q.next
                p = p.next
                
            p.next = t
            p = p.next
            t = t.next
        if q:
            p.next = q
        return list1.next

# @lc code=end

# if __name__ == '__main__':
#     l1 = [5,8]
#     l2 = [2,3,4,9]

#     s = Solution()
#     list1 = s.create_list(l1)
#     list2 = s.create_list(l2)

#     p = s.mergeTwoLists(list1, list2)

#     print(s.print_link(p))



