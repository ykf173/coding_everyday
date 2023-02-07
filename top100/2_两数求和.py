'''
2. 两数相加
给你两个 非空 的链表，表示两个非负的整数。它们每位数字都是按照 逆序 的方式存储的，并且每个节点只能存储 一位 数字。

请你将两个数相加，并以相同形式返回一个表示和的链表。

你可以假设除了数字 0 之外，这两个数都不会以 0 开头。



示例 1：


输入：l1 = [2,4,3], l2 = [5,6,4]
输出：[7,0,8]
解释：342 + 465 = 807.
示例 2：

输入：l1 = [0], l2 = [0]
输出：[0]
示例 3：

输入：l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
输出：[8,9,9,9,0,0,0,1]


提示：

每个链表中的节点数在范围 [1, 100] 内
0 <= Node.val <= 9
题目数据保证列表表示的数字不含前导零
'''
import copy


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def creat_l(l: list):
    head = ListNode(l[0])
    p = head
    for val in l[1:]:
        s = ListNode(val)
        p.next = s
        p = p.next
    return head


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        p = l1
        next_add = 0
        while l2:
            if not l1.next and l2 and l1.val + l2.val + next_add > 9:
                s = ListNode()
                l1.next = s
                l1 = s
            if l1.val + l2.val + next_add > 9:
                l1.val = l1.val + l2.val + next_add - 10
                next_add = 1
            else:
                l1.val += l2.val + next_add
                next_add = 0
            l2 = l2.next

            if l1.next:
                l1 = l1.next

        # while l2:
        #     if next_add + l2.val > 9:
        #         s = ListNode(next_add + l2.val - 10)
        #         next_add = 1
        #     else:
        #         s = ListNode(l2.val + next_add)
        #         next_add = 0
        #     l1.next = s
        #     l1 = s
        #     l2 = l2.next

        while l1:  # l1遍历完毕
            if l1.val + next_add > 9:
                l1.val = l1.val + next_add - 10
                next_add = 1
            else:
                l1.val += next_add
                next_add = 0
            if not l2 and not l1.next and next_add:  # 最后一位
                s = ListNode(next_add)
                l1.next = s
                l1 = s
            l1 = l1.next

        return p


if __name__ == '__main__':
    s = Solution()
    l1 = [2, 4, 3]
    l2 = [5, 6, 4]
    l1 = [2, 4, 9]
    l2 = [5, 6, 4, 9, 6]
    # l1 = [9, 9, 1]
    # l2 = [1]
    # l1 = [0]
    # l2 = [0]
    # l1 = [9, 9, 9, 9, 9, 9, 9]
    # l2 = [9, 9, 9, 9]
    l1 = creat_l(l1)
    l2 = creat_l(l2)
    q = s.addTwoNumbers(l1, l2)
    while q:
        print(q.val, end=' ')
        q = q.next
        if q:
            print('-> ', end='')
