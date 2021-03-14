from typing import List


class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        size = len(nums)
        if size <= 0:
            self.sumNums = [0]
        else:
            self.sumNums = [nums[0]]
            for i in range(1, size):
                self.sumNums.append(nums[i] + self.sumNums[i - 1])

    def sumRange(self, i: int, j: int) -> int:
        if not self.nums:
            return 0
        elif len(self.nums) == 1:
            return self.nums[0]

        return self.sumNums[j] - self.sumNums[i] + self.nums[i]


# Your NumArray object will be instantiated and called as such:
nums = [-2]
obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
print(obj.sumRange(0, 1))
# print(obj.sumRange(2, 5))
# print(obj.sumRange(0, 5))
