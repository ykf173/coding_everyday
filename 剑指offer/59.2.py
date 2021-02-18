import collections
import queue


class MaxQueue:

    def __init__(self):
        self.sequence = queue.Queue()
        self.deQueue = collections.deque()

    def max_value(self) -> int:
        if self.deQueue:
            return self.deQueue[0]
        else:
            return -1

    def push_back(self, value: int) -> None:
        self.sequence.put(value)
        while self.deQueue and self.deQueue[-1] < value:
            self.deQueue.pop()
        self.deQueue.append(value)

    def pop_front(self) -> int:
        if self.sequence.empty():
            return -1
        topValue = self.sequence.get()
        if self.sequence:
            if self.deQueue[0] == topValue:
                self.deQueue.popleft()
            return topValue


# Your MaxQueue object will be instantiated and called as such:
obj = MaxQueue()
print(obj.max_value())
print(obj.push_back(43))
print(obj.pop_front())
print(obj.max_value())



'''
["MaxQueue","push_back","push_back","max_value","pop_front","max_value"]
[[],[1],[2],[],[],[]]
["MaxQueue","pop_front","max_value"]
[[],[],[]]
'''

'''
["MaxQueue","max_value","pop_front","max_value","push_back","max_value","pop_front","max_value","pop_front","push_back","pop_front","pop_front","pop_front","push_back","pop_front","max_value","pop_front","max_value","push_back","push_back","max_value","push_back","max_value","max_value","max_value","push_back","pop_front","max_value","push_back","max_value","max_value","max_value","pop_front","push_back","push_back","push_back","push_back","pop_front","pop_front","max_value","pop_front","pop_front","max_value","push_back","push_back","pop_front","push_back","push_back","push_back","push_back","pop_front","max_value","push_back","max_value","max_value","pop_front","max_value","max_value","max_value","push_back","pop_front","push_back","pop_front","max_value","max_value","max_value","push_back","pop_front","push_back","push_back","push_back","pop_front","max_value","pop_front","max_value","max_value","max_value","pop_front","push_back","pop_front","push_back","push_back","pop_front","push_back","pop_front","push_back","pop_front","pop_front","push_back","pop_front","pop_front","pop_front","push_back","push_back","max_value","push_back","pop_front","push_back","push_back","pop_front"]
[[],[],[],[],[46],[],[],[],[],[868],[],[],[],[525],[],[],[],[],[123],[646],[],[229],[],[],[],[871],[],[],[285],[],[],[],[],[45],[140],[837],[545],[],[],[],[],[],[],[561],[237],[],[633],[98],[806],[717],[],[],[186],[],[],[],[],[],[],[268],[],[29],[],[],[],[],[866],[],[239],[3],[850],[],[],[],[],[],[],[],[310],[],[674],[770],[],[525],[],[425],[],[],[720],[],[],[],[373],[411],[],[831],[],[765],[701],[]]

[null,-1,-1,-1,null,46,46,-1,-1,null,868,-1,-1,null,525,-1,-1,-1,null,null,868,null,868,868,868,null,123,871,null,871,871,871,646,null,null,null,null,229,871,871,285,45,871,null,null,140,null,null,null,null,837,871,null,871,871,545,871,871,871,null,561,null,237,871,871,871,null,633,null,null,null,98,871,806,871,871,871,717,null,186,null,null,268,null,29,null,866,239,null,3,850,310,null,null,871,null,674,null,null,770]
[null,-1,-1,-1,null,46,46,-1,-1,null,868,-1,-1,null,525,-1,-1,-1,null,null,646,null,646,646,646,null,123,871,null,871,871,871,646,null,null,null,null,229,871,837,285,45,837,null,null,140,null,null,null,null,837,806,null,806,806,545,806,806,806,null,561,null,237,806,806,806,null,633,null,null,null,98,866,806,866,866,866,717,null,186,null,null,268,null,29,null,866,239,null,3,850,310,null,null,770,null,674,null,null,770]
'''
