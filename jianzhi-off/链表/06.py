from typing import List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class LinkList:
    def __init__(self, head=None):
        self.head = head

    def createList(self, li):
        if len(li) > 1:
            self.head = ListNode(li[0])
        tempNode = self.head
        for x in li[1:]:
            node = ListNode(x)
            tempNode.next = node
            tempNode = node


class Solution:
    def reversePrint(self, head: ListNode) -> List[int]:
        values = []
        p = head
        while p:
            values.append(p.val)
            p = p.next
        return values[::-1]


if __name__ == '__main__':
    s = Solution()
    while 1:
        li = list(input().split(','))
        linked = LinkList()
        linked.createList(li)
        print(s.reversePrint(linked.head))

'''
1,2,3
3,4,56,7,8,9,l
'''
