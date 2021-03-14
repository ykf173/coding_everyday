'''
输入一个整型数组，数组中的一个或连续多个整数组成一个子数组。求所有子数组的和的最大值。
要求时间复杂度为O(n)。
'''

from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        size = len(nums)
        maxValue = [nums[0]]
        for i in range(1, size):
            maxValue.append(max(maxValue[i - 1] + nums[i], nums[i]))
        return max(maxValue)

if __name__ == '__main__':
    s = Solution()
    while 1:
        nums = list(eval(input()))
        print(s.maxSubArray(nums))

'''
[-2,1,-3,4,-1,2,1,-5,4]
[1,1,1,1,1,1,1]
[-1,-1,-1,-1,-1,-1]

'''