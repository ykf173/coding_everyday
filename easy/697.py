import collections
from typing import List


class Solution:
    '''
    给定一个非空且只包含非负数的整数数组 nums，数组的度的定义是指数组里任一元素出现频数的最大值。
    你的任务是在 nums 中找到与 nums 拥有相同大小的度的最短连续子数组，返回其长度。
    '''
    def findShortestSubArray(self, nums: List[int]) -> int:
        size = len(nums)
        numsDict = collections.Counter(nums)
        maxCounter = max(numsDict.values())
        maxValues = {}
        ans, i = 50000, 0
        for key, val in numsDict.items():
            if val == maxCounter:
                maxValues[key] = i
                i += 1

        maxSize = len(maxValues)
        pos = [[] for _ in range(maxSize)]
        for i in range(size):
            if nums[i] in maxValues:
                pos[maxValues[nums[i]]].append(i)

        for i in range(maxSize):
            ans = min(ans, pos[i][-1] - pos[i][0] + 1)

        return ans


if __name__ == '__main__':
    s = Solution()
    while 1:
        nums = list(map(int, input().split(',')))
        print(s.findShortestSubArray(nums))

'''
1, 2, 2, 3, 1
1,2,2,3,1,4,2
1,1,1,1,1,1,1
1,2,3,4,5,6,7
ans: [2, 6, 7, 1]

'''
