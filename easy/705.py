N = 1000001  # 质数


class MyHashSet1:
    '''
    大数组法，占用空间太大
    '''

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.set = [False] * N

    def add(self, key: int) -> None:
        self.set[key] = True

    def remove(self, key: int) -> None:
        self.set[key] = False

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        return self.set[key]


class MyHashSet:
    '''
    链表解决冲突，使用数组，类似二维数组，但不一样，先找列，后找行
    '''

    def __init__(self):
        """
        数据分桶
        """
        self.buckets = 1009
        self.eleSet = [[] for _ in range(self.buckets)]

    def hash(self, key):  # 桶内
        return key % self.buckets

    def add(self, key: int) -> None:
        curBuckets = self.hash(key)
        if key in self.eleSet[curBuckets]:
            return None
        self.eleSet[curBuckets].append(key)

    def remove(self, key: int) -> None:
        curBuckets = self.hash(key)
        if key not in self.eleSet[curBuckets]:
            return None
        self.eleSet[self.hash(key)].remove(key) #利用列表自动寻址

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        curBuckets = self.hash(key)
        return key in self.eleSet[curBuckets]

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
