'''
动态规划
连续子数组最大积
给你一个整数数组 nums ，请你找出数组中乘积最大的连续子数组（该子数组中至少包含一个数字），并返回该子数组所对应的乘积。
'''

import copy
from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        size = len(nums)
        ans = maxF = minF = nums[0]
        for i in range(1, size):
            mn, mx = minF, maxF
            maxF = max(maxF * nums[i], max(nums[i], mn * nums[i]))
            minF = min(minF * nums[i], min(nums[i], mx * nums[i]))
            ans = max(ans, maxF)
        return ans

    def maxProduct1(self, nums: List[int]) -> int:
        '''
        动态规划：存储最大最小值
        :param nums:
        :return:
        '''
        size = len(nums)
        curMax = copy.deepcopy(nums)
        curMin = copy.deepcopy(nums)

        for i in range(1, size):
            curMax[i] = max(curMax[i - 1] * nums[i], max(nums[i], curMin[i - 1] * nums[i]))
            curMin[i] = min(curMin[i - 1] * nums[i], min(nums[i], curMax[i - 1] * nums[i]))

        return max(curMax)