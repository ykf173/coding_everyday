"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
import copy


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:

    def __init__(self):
        self.visitedDic = {}

    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return head

        current = head
        while current:
            self.visitedDic[current] = Node(current.val)
            current = current.next

        current = head
        while current:
            self.visitedDic[current].next = self.visitedDic.get(current.next)
            self.visitedDic[current].random = self.visitedDic.get(current.random)
            current = current.next

        return self.visitedDic[head]

    def copyRandomList1(self, head: 'Node') -> 'Node':
        if not head:
            return head

        if head in self.visitedDic:
            return self.visitedDic[head]

        node = Node(head.val)

        self.visitedDic[head] = node

        node.next = self.copyRandomList1(head.next)
        node.random = self.copyRandomList1(head.random)

        return node
