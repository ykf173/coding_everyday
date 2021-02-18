class ListNode():
    def __init__(self, val):
        if isinstance(val, int):
            self.val = val
            self.next = None

        elif isinstance(val, list):
            self.val = val[0]
            self.next = None
            cur = self
            for i in val[1:]:
                cur.next = ListNode(i)
                cur = cur.next

    def gatherAttrs(self):
        return ", ".join("{}: {}".format(k, getattr(self, k)) for k in self.__dict__.keys())

    def __str__(self):
        return self.__class__.__name__ + " {" + "{}".format(self.gatherAttrs()) + "}"

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if isinstance(l1, list):
            l1 = ListNode(l1)
            l2 = ListNode(l2)
        if isinstance(l1, int):
            l1 = ListNode(l1)
            l2 = ListNode(l2)

        carry = 0
        restemper = ListNode(0)
        res = restemper
        while l1 or l2:
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            s = x + y + carry
            carry = s // 10
            restemper.next = ListNode(s % 10)
            restemper = restemper.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        if carry > 0:
            restemper.next = carry
        return res.next


# @lc code=end
if __name__ == "__main__":
    test = Solution()
    print(test.addTwoNumbers([5,6], [5,7]))
