#
# @lc app=leetcode.cn id=148 lang=python3
#
# [148] 排序链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    #     p = ListNode(-1000, list1)
    def create_list(self, l):
        head = ListNode()
        p = head
        if not l:
            return head
        for num in l:
            node = ListNode(num)
            p.next = node
            p = p.next
        return head.next
    
    def print_link(self, q):
        p = q
        while p:
            print(p.val, end='')
            
    def quick_sort(self, nums) -> list:
        n = len(nums)
        if n <= 1:
            return nums

        mid = n // 2


        left, right, mid_nums = [], [], []
        for i in range(n):
            if nums[i] < nums[mid]:
                left.append(nums[i])
            elif nums[i] > nums[mid]:
                right.append(nums[i])
            else:
                mid_nums.append(nums[i])

        return self.quick_sort(left) + mid_nums + self.quick_sort(right)


    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        nums = []
        p = head
        while p:
            nums.append(p.val)
            p = p.next
        nums = self.quick_sort(nums)

        head = ListNode(nums[0])
        p = head
        for i in range(len(nums)):
            q = ListNode(nums[i])
            p.next = q
            p = q

        return head.next

        
# @lc code=end

