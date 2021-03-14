class MyHashMap:
    '''
    取模
    '''

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.buckets = 1000
        self.curBuckets = 1001
        self.dict = [[-1] * self.buckets for _ in range(self.curBuckets)]

    def hash(self, key):
        return key % self.buckets

    def pos(self, key):
        return key // self.buckets


    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        curBuckets = self.hash(key)
        self.dict[self.pos(key)][curBuckets] = value

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        curBuckets = self.hash(key)
        return self.dict[self.pos(key)][curBuckets]

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        curBuckets = self.hash(key)
        self.dict[self.pos(key)][curBuckets] = -1


# Your MyHashMap object will be instantiated and called as such:
obj = MyHashMap()
obj.put(1, 1)
obj.put(1, 1)
param_2 = obj.get(1)
print(param_2)
obj.remove(2)
# print(obj.dict)
