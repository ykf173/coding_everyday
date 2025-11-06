# Definition for singly-linked list.
import copy


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

    def printLinkList(self, head):
        while head:
            print(head.val)
            head = head.next


class Solution:
    def reverseListX(self, head: ListNode) -> ListNode:
        '''
        超时，可能是deepcopy的原因
        :param head:
        :return:
        '''
        rear = head
        flag = True

        while rear:
            temp = rear
            if flag:
                head = rear
                head.next = None
                flag = False
            else:
                temp.next = head
                head = temp
            rear = rear.next

        return head

    def reverseList(self, head: ListNode) -> ListNode:
        cur, pre = head, None

        while cur:
            temp = cur.next
            cur.next = pre
            pre = cur
            cur = temp

        return pre


if __name__ == '__main__':
    s = Solution()
    while 1:
        li = list(input().split(','))
        linked = LinkList()
        linked.createList(li)
        print(linked.printLinkList(linked.head))
        print(s.reverseList(linked.head))
        print(linked.printLinkList(s.reverseList(linked.head)))

'''
1,2,3,4,5
'''
