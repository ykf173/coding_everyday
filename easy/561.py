from typing import List


class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums = sorted(nums)
        size = len(nums)
        minTotalValue = 0
        for i in range(0, size, 2):
            minTotalValue += min(nums[i], nums[i + 1])

        return minTotalValue


if __name__ == '__main__':
    s = Solution()
    while 1:
        nums = list(map(int, input().split(',')))
        print(s.arrayPairSum(nums))


'''
1,4,3,2
1,2,3,4
3,4,2,1
6,2,6,5,1,2
1,2
'''