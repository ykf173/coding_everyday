'''
leetcode 剑指offer第9题
使用两个栈实现队列
思想：使用一个空栈作为辅助栈，出栈时逆置原来的栈。

'''

class CQueue:

    def __init__(self):
        self.stack1, self.stack2 = [], []

    def appendTail(self, value: int) -> None:
        self.stack1.append(value)

    def deleteHead(self) -> int:
        if self.stack2:
            return self.stack2.pop()
        if not self.stack1:
            return -1
        while self.stack1:
            self.stack2.append(self.stack1.pop())
        return self.stack2.pop()
# Your CQueue object will be instantiated and called as such:
# obj = CQueue()
# obj.appendTail(value)
# param_2 = obj.deleteHead()
