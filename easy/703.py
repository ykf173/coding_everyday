from typing import List


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = sorted(nums, reverse=True)

    def add(self, val: int) -> int:
        size = len(self.nums)
        if not self.nums:
            self.nums.append(val)
        if val < self.nums[size - 1]:
            self.nums.insert(size, val)
        else:
            for i in range(len(self.nums)):
                if self.nums[i] <= val:
                    self.nums.insert(i, val)
                    break

        return self.nums[self.k - 1]


# Your KthLargest object will be instantiated and called as such:
if __name__ == '__main__':
    k = int(input())
    nums = list(map(int, input().split(',')))
    obj = KthLargest(k, nums)
    while 1:
        val = int(input())
        print(obj.add(val))
        print(obj.nums)

'''
3
4,5,8,2
3
5
10
9
4

1,[]
-3
-2
-4
0
4

3
1,1
1
1
3
3
3
4
4
4
'''
